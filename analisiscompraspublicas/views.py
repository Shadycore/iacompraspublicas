from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, F, DateTimeField, Count, FloatField, \
                            IntegerField, Prefetch, Case, When, Avg, Min, \
                            Max, Value, Avg, StdDev
from datetime import datetime, timezone, timedelta, date
from django.db.models.functions import TruncMonth, TruncYear, ExtractMinute, \
                            ExtractMonth, ExtractYear, Cast, Coalesce, Extract, \
                            Concat, NullIf
from django.db.models.query import Q
import json
import math
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from analisiscompraspublicas.models import contract, tender, planning, award, release


def contratosView(request):
    template_name = 'contratos.html'
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))
    mensaje = ""
    anio_anterior = dFecha - 1
    average_value = 0
    std_deviation = 0
    average_value_anterior = 0
    std_deviation_anterior = 0
    contratos_estados = {}
    contratos_mayor_valor = {}
    try:          
        ## Contratos
        #info anio combo    
        contracts = contract.objects.filter(Q(amount__isnull=False) & Q(amount__gt=0) & Q(contractPeriod_startDate__startswith=dFecha))
        
        average_value = contracts.annotate(numeric_amount=Cast(NullIf('amount', 
                                                                            Value('')), output_field=FloatField())).aggregate(avg_value=Avg('numeric_amount'))['avg_value']
        
        std_values = contracts.annotate(numeric_amount=Cast(NullIf('amount', Value('')),output_field=IntegerField()))

        a =[ i for i in std_values.values_list('numeric_amount', flat=True).exclude(numeric_amount=None) ]
        std_deviation = _std_deviation(a)

        average_value = int(average_value)
        std_deviation = std_deviation
        #info anio combo - 1

        contracts = contract.objects.filter(Q(amount__isnull=False) & Q(amount__gt=0) & Q(contractPeriod_startDate__startswith=anio_anterior))
        
        average_value_anterior = contracts.annotate(numeric_amount=Cast(NullIf('amount', 
                                                                            Value('')), output_field=FloatField())).aggregate(avg_value=Avg('numeric_amount'))['avg_value']
        
        std_values_anterior = contracts.annotate(numeric_amount=Cast(NullIf('amount', Value('')),output_field=IntegerField()))

        a =[ i for i in std_values_anterior.values_list('numeric_amount', flat=True).exclude(numeric_amount=None) ]
        std_deviation_anterior = _std_deviation(a)

        average_value_anterior = int(average_value_anterior)
        std_deviation_anterior = std_deviation_anterior
        ## Contratos por estados
        contracts_status = contract.objects.filter(Q(amount__isnull=False) & Q(amount__gt=0) & Q(contractPeriod_startDate__startswith=dFecha))
        if not contracts_status:
            contratos_estados = {'status': "", 'contador': 0}
        else:
            #agrupa los contratos por estado y los cuenta
            contratos_estados = contracts_status.values('status').annotate(contador=Count('co_id')).order_by('-contador')

        #selecciona los 5 contrato con mayor valor y el estado del mismo, se filtra por el año actual
        contratos_mayor_valor = contract.objects.filter(Q(amount__isnull=False) & Q(amount__gt=0) & Q(contractPeriod_startDate__startswith=dFecha) & Q(status="active")).order_by('-amount')[:5]
        if not contratos_mayor_valor:
            contratos_mayor_valor = {}


    except Exception as e:
        average_value = 0
        std_deviation = 0
        average_value_anterior = 0
        std_deviation_anterior = 0
        contratos_estados = {'status': "", 'contador': 0}
        contratos_mayor_valor = {}
        mensaje = e.__str__()
    finally:
        anios = 2014 
        oanios = [i for i in range(anioactual, anios, -1)]

    context = {'anios': oanios, 'ianio': dFecha, 'anioactual': anioactual, 'anio_anterior': anio_anterior,
               'valorpromedio': average_value, 'desviacionstandar': std_deviation,
               'valorpromedio_anterior': average_value_anterior, 'desviacionstandar_anterior': std_deviation_anterior, 
                 'contratos_estados': contratos_estados, 'contratos_mayor_valor': contratos_mayor_valor,'mensaje': mensaje}

    return render(request, template_name, context)


def compradoresView(request):
    template_name = 'compradores.html'
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))
    
    mensaje = ""
    anio_anterior = dFecha - 1
    context = {}
    entidades_activas = {}
    metodos = {}
    years = []
    num_contratos = []
    tendencias = {}
    promedios = {}
    mensaje = ""


    try:
        #seleccionar los 5 compradores con mayor numero de contratos activos, sumar los montos y filtrar por año actual
        entidades_activas = tender.objects.filter(Q(value_amount__isnull=False) & Q(value_amount__gt=0) & Q(tenderPeriod_startDate__startswith=dFecha)).values('procuringEntity_name').annotate(contador=Count('te_id')).order_by('-contador')[:5]
        
        # Obtener los métodos de adquisición más comunes y la cantidad de los mismos.
        metodos = tender.objects.filter(Q(procurementMethod__isnull=False) & Q(procurementMethod__gt=0) & Q(tenderPeriod_startDate__startswith=dFecha)).values('procurementMethod').annotate(contador=Count('te_id')).order_by('-contador')

        # obtener las licitaciones por año y por mainProcurementCategory obtener la cantidad de las licitaciones
        tendencias = tender.objects.filter(Q(mainProcurementCategory__isnull=False) & Q(mainProcurementCategory__gt=0) & Q(tenderPeriod_startDate__startswith=dFecha)).values('mainProcurementCategory').annotate(contador=Count('te_id')).order_by('mainProcurementCategory')

        # Calcular el promedio de días, awardPeriod_durationInDays, que duran las licitaciones en cada una de lascategorías mainProcurementCategory
        promedios = tender.objects.filter(Q(mainProcurementCategory__isnull=False) & Q(mainProcurementCategory__gt=0) & Q(tenderPeriod_startDate__startswith=dFecha)).values('mainProcurementCategory').annotate(promedio=Avg('awardPeriod_durationInDays')).order_by('mainProcurementCategory')
    except Exception as e: 
        entidades_activas = {}
        metodos = {}
        mensaje = e.__str__()
        tendencias = {}
        promedios = {}
        years = []
        num_contratos = []

    finally:
        anios = 2014 
        oanios = [i for i in range(anioactual, anios, -1)]
        context = {'entidades_activas': entidades_activas}

    context = {'anios': oanios, 'ianio': dFecha, 'anioactual': anioactual, 'anio_anterior': anio_anterior,
               'entidades_activas': entidades_activas, 'years':years, 'num_contratos': num_contratos,
                'metodos': metodos, 'tendencias': tendencias, 'promedios': promedios, 'mensaje': mensaje}
    return render(request, template_name, context)




##funciones locales
def _std_deviation(values):
    # Calcula la media (promedio) de los valores
    mean = sum(values) / len(values)

    # Calcula la suma de los cuadrados de las diferencias entre cada valor y la media
    squared_diff = [(x - mean) ** 2 for x in values]

    # Calcula la varianza como el promedio de los cuadrados de las diferencias
    variance = sum(squared_diff) / len(values)

    # Calcula la desviación estándar como la raíz cuadrada de la varianza
    std_dev = math.sqrt(variance)

    return int(std_dev)

