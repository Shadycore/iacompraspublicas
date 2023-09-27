from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.db import connection
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, F, DateTimeField, Count, FloatField, \
                            IntegerField, Prefetch, Case, When, Avg, Min, \
                            Max, Value, Avg, StdDev, CharField, Func
from datetime import datetime, timezone, timedelta, date
from django.db.models.functions import TruncMonth, TruncYear, ExtractMinute, \
                            ExtractMonth, ExtractYear, Cast, Coalesce, Extract, \
                            Concat, NullIf, Substr
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
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#import statsmodels.api as sm
#from statsmodels.tsa.arima_model import ARIMA


from analisiscompraspublicas.models import contract, tender, planning, award, release, supplier


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

        contracts_status = contract.objects.filter(Q(amount__isnull=False) & Q(amount__gt=0) & Q(contractPeriod_startDate__startswith=dFecha))
        if not contracts_status:
            contratos_estados = {'status': "", 'contador': 0}
        else:
            contratos_estados = contracts_status.values('status').annotate(contador=Count('co_id')).order_by('-contador')

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
        entidades_activas = tender.objects.filter(Q(value_amount__isnull=False) & Q(value_amount__gt=0) & Q(tenderPeriod_startDate__startswith=dFecha)).values('procuringEntity_name').annotate(contador=Count('te_id')).order_by('-contador')[:5]
        
        metodos = tender.objects.filter(Q(procurementMethod__isnull=False) & Q(procurementMethod__gt=0) & Q(tenderPeriod_startDate__startswith=dFecha)).values('procurementMethod').annotate(contador=Count('te_id')).order_by('-contador')

        tendencias = tender.objects.filter(Q(mainProcurementCategory__isnull=False) & Q(mainProcurementCategory__gt=0) & Q(tenderPeriod_startDate__startswith=dFecha)).values('mainProcurementCategory').annotate(contador=Count('te_id')).order_by('mainProcurementCategory')

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
        

    context = {'anios': oanios, 'ianio': dFecha, 'anioactual': anioactual, 'anio_anterior': anio_anterior,
               'entidades_activas': entidades_activas, 'years':years, 'num_contratos': num_contratos,
                'metodos': metodos, 'tendencias': tendencias, 'promedios': promedios, 'mensaje': mensaje}
    return render(request, template_name, context)

def compradores2View (request):
    template_name = 'compradores2.html'
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))
    
    mensaje = ""
    anio_anterior = dFecha - 1
    context = {}
    top_categories = {}
    amount_categories = {}
    tendencias_categories = {}
    promedio_dias = {}

    queryset = tender.objects.annotate(
        start_date_year=Substr('tenderPeriod_startDate', 1, 4, output_field=CharField())
    ).filter(start_date_year__regex=r'^\d{4}$')  

    result = queryset.values('start_date_year', 'procurementMethod').annotate(
        count_te_id=Count('te_id')
    ).order_by('start_date_year', 'procurementMethod')

    aggregated_data = {}
    for entry in result:
        year = entry['start_date_year']
        method = entry['procurementMethod']
        num_te_id = entry['count_te_id']
        if year not in aggregated_data:
            aggregated_data[year] = {}
        aggregated_data[year][method] = num_te_id

    # Convierte los datos a un formato que se pueda usar en JavaScript
    js_data = {
        'labels': list(aggregated_data.keys()),
        'datasets': []
    }
    methods = set()
    for year_data in aggregated_data.values():
        methods.update(year_data.keys())

    for method in methods:
        dataset = {
            'label': method,
            'data': [year_data.get(method, 0) for year_data in aggregated_data.values()],
        }
        js_data['datasets'].append(dataset)

    # Convierte los datos de Python a JSON
    js_data_json = json.dumps(js_data)
    try:
        
        top_categories = tender.objects.values('procurementMethod').annotate(
            num_contratos=Count('te_id')
        ).exclude(
            Q(procurementMethod__isnull=True) | Q(procurementMethod='USD')
        ).order_by('-num_contratos')
        
        amount_categories = tender.objects.values('procurementMethod').annotate(
            valor_contratos=Sum('value_amount')
        ).exclude(
            Q(procurementMethod__isnull=True) | Q(procurementMethod='USD')
        ).order_by('-valor_contratos')

        tendencias_categories = tender.objects.values('procurementMethod').annotate(
            num_contratos=Count('te_id')
        ).exclude(
            Q(procurementMethod__isnull=True) | Q(procurementMethod='USD')
        ).order_by('-num_contratos')

        promedio_dias = tender.objects.annotate(
            duration=Cast('tenderPeriod_durationInDays', output_field=FloatField())
        ).values('procurementMethod').exclude(
            Q(procurementMethod__isnull=True) | Q(procurementMethod='USD')
        ).annotate(
            avg_dias=Avg('duration')
        )
    except Exception as e:
        mensaje = e.__str__()
        top_categories = {}
        amount_categories = {}
        tendencias_categories = {}
        promedio_dias = {}
    finally:
        anios = 2014 
        oanios = [i for i in range(anioactual, anios, -1)]


    context = {'anios': oanios, 'ianio': dFecha, 'anioactual': anioactual, 'anio_anterior': anio_anterior,
               'top_categories': top_categories, 'amount_categories': amount_categories,
               'tendencias_categories': tendencias_categories , 'promedio_dias': promedio_dias ,
               'result': result, 'js_data_json': js_data_json , 'mensaje': mensaje}

    return render (request, template_name, context)

def proveedoresView(request):
    template_name = 'proveedores.html'
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))
    
    mensaje = ""
    anio_anterior = dFecha - 1
    context = {}
    results = {}
    try:
        query = f"""
            SELECT a.name AS nombre_proveedor,
                b.status AS estado_contrato,
                SUBSTRING(b.dateSigned, 1, 4) AS anio_contrato,
                SUM(CAST(b.amount AS FLOAT)) AS total_contratos,
                COUNT(b.ocid) AS cantidad_contratos
            FROM supplier a
            INNER JOIN contract b ON a.ocid = b.ocid
            WHERE SUBSTRING(b.dateSigned, 1, 4) = '{dFecha}'
            GROUP BY SUBSTRING(b.dateSigned, 1, 4), a.name, b.status
            ORDER BY b.status asc;
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()    
    
    except Exception as e: 
            results = {}
            mensaje = e.__str__()
    finally:
        anios = 2014 
        oanios = [i for i in range(anioactual, anios, -1)]

    context = {'anios': oanios, 'ianio': dFecha, 'anioactual': anioactual, 'anio_anterior': anio_anterior,
               'results': results, 'mensaje': mensaje}
    return render(request, template_name, context)

def analisisvariosView(request):
    template_name = 'varios.html'
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    mensaje = ""
    anio_anterior = dFecha - 1
    context = {}

    return render(request, template_name, context)   

def tendencia_contratos(request):
    dFecha = datetime.now().year
    query = f"""
            select ocid, cast(amount as float) as amount, substr(dateSigned,1,4) as dateSigned
            from contract;
        """

    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()   
    column_names = [desc[0] for desc in cursor.description]
    contracts = [dict(zip(column_names, row)) for row in results]

    df = pd.DataFrame(contracts)
    df['dateSigned'] = pd.to_datetime(df['dateSigned'])
    df['dateSigned'] = df['dateSigned'].dt.year
    contract_amount_by_year = df.groupby(['dateSigned'])['amount'].sum()

    plt.figure(figsize=(12, 6))
    plt.plot(contract_amount_by_year.index, contract_amount_by_year.values, marker='o')
    plt.title('Evolución de Montos de Contratos a lo Largo de los Años')
    plt.xlabel('Año')
    plt.ylabel('Monto Total de Contratos')
    plt.grid(True)
    # Convierte el gráfico en una imagen
    canvas = FigureCanvas(plt.gcf())
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)

    return response

def grafico_arima(request):
    query = f"""
            select cast(tenderPeriod_startDate as datetime) as Year,
                cast(value_amount as float) as value_amount
            from tender
        """
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        tenders = cursor.fetchall()   

    column_names = [desc[0] for desc in cursor.description]
    tenders_data = [dict(zip(column_names, row)) for row in tenders]
    
    tender_df = pd.DataFrame(list(tenders_data))
    tender_df['Year'] = pd.to_datetime(tender_df['Year'])  # Asegúrate de que 'dateSigned' sea un objeto DateTime

    # Establece la fecha como índice
    tender_df.set_index('Year', inplace=True)

    # Reemplaza los valores faltantes (NaN) con ceros o el método de tu elección.
    tender_df['value_amount'].fillna(0, inplace=True)

    # Realiza un análisis visual de los datos
    plt.figure(figsize=(15, 8))
    plt.plot(tender_df.index, tender_df['value_amount'], label='Costo de licitaciones')
    plt.title('Costo de licitaciones a lo largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)
    #plt.show()

    # Ajusta un modelo ARIMA
    order = (1, 0, 1)  # Define los valores p, d, q adecuados para tu modelo
    model = ARIMA(tender_df['value_amount'], order=order)
    results = model.fit()

    # Realiza predicciones
    forecast_steps = 12  # Número de pasos de predicción hacia el futuro
    forecast, stderr, conf_int = results.forecast(steps=forecast_steps)

    # Crea un gráfico de las predicciones
    plt.figure(figsize=(15, 8))
    plt.plot(tender_df.index, tender_df['value_amount'], label='Costo de licitaciones')
    plt.plot(pd.date_range(start=tender_df.index[-1], periods=forecast_steps+1, closed='right'), forecast, label='Predicción', color='red')
    plt.title('Predicción de Costo de licitaciones')
    plt.xlabel('Fecha')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)

    #plt.show()
    # Convierte el gráfico en una imagen
    canvas = FigureCanvas(plt.gcf())
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    """
    response = HttpResponse(content_type='image/png')
    return response

def tendencia_valor_contrato(request):
    dFecha = datetime.now().year
    query = f"""
            select 
            SUBSTR(contractPeriod_startDate,1,4) as year,
            SUBSTR(contractPeriod_startDate,6,2) as month,
            sum(amount) as total_contract_value
            from contract
            group by SUBSTR(contractPeriod_startDate,1,4),
                    SUBSTR(contractPeriod_startDate,6,2)
        """

    with connection.cursor() as cursor:
        cursor.execute(query)
        contracts = cursor.fetchall()   

    column_names = [desc[0] for desc in cursor.description]
    data = [dict(zip(column_names, row)) for row in contracts]

    # Crear un DataFrame de Pandas a partir de los datos
    df = pd.DataFrame(data)

    df['Fecha'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

    # Establecer la columna 'Fecha' como índice (necesario para el análisis de series temporales)
    df.set_index('Fecha', inplace=True)

    # Graficar las tendencias
    plt.figure(figsize=(15, 8))
    plt.plot(df.index, df['total_contract_value'], marker='o', linestyle='-')
    plt.title('Tendencias en el Valor de Contratos a lo largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Valor del Contrato')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar el gráfico en un archivo o mostrarlo
    # plt.savefig('tendencias_contratos_publicos.png')
    #plt.show()
    # Convierte el gráfico en una imagen
    canvas = FigureCanvas(plt.gcf())
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)

    return response

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

