from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
import csv
import io
import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate
import shutil
from django.conf import settings
from django.db.models import Q
import tempfile

from analizaproveedor.models import solicitud_compra, sri_ente


def CargaInfoView(request):
    template_name = "cargainfo/cargainfo.html"
    context = {}    

    if request.method == 'POST':
        csv_file = request.FILES['archivo_csv']
        # validar el nombre del archivo en los primeros 7 caracteres
        if csv_file.name[:7] == "SRI_RUC":
            cargar_info_sri(csv_file, request.user, "|")
        
        if csv_file.name[:7] == "awards_":
            cargar_info_csv(csv_file, request.user, ",")

    return render(request, template_name, context)


def cargar_info_sri (csv_file, user, separador):

    with open(file_name.name, 'r',) as file_name:
        reader = csv.reader(file_name)
        next(reader)
        for line in reader:
            #Lee información
            columns = line.split(separador)
            numero_ruc = columns[0]
            razon_social = columns[1]
            provincia_jurisdiccion = columns[2]
            nombre_comercial = columns[3]
            estado_contribuyente = columns[4]
            clase_contribuyente = columns[5]
            fecha_inicio_actividades = columns[6]
            fecha_actualizacion = columns[7]
            fecha_suspension_definitiva = columns[8]
            fecha_reinicio_actividades = columns[9]
            obligado = columns[10]
            tipo_contribuyente = columns[11]
            numero_establecimiento = columns[12]
            nombre_fantasia_comercial = columns[13]
            estado_establecimiento = columns[14]
            descripcion_provincia_est = columns[15]
            descripcion_canton_est = columns[16]
            descripcion_parroquia_est = columns[17]
            codigo_ciiu = columns[18]
            actividad_economica = columns[19]

            # Guarda solicitud de compra
            _sri_ente = sri_ente(
                numero_ruc = numero_ruc,
                razon_social = razon_social,
                provincia_jurisdiccion = provincia_jurisdiccion,
                nombre_comercial = nombre_comercial,
                estado_contribuyente = estado_contribuyente,
                clase_contribuyente = clase_contribuyente,
                fecha_inicio_actividades = fecha_inicio_actividades,
                fecha_actualizacion = fecha_actualizacion,
                fecha_suspension_definitiva = fecha_suspension_definitiva,
                fecha_reinicio_actividades = fecha_reinicio_actividades,
                obligado = obligado,
                tipo_contribuyente = tipo_contribuyente,
                numero_establecimiento = numero_establecimiento,
                nombre_fantasia_comercial = nombre_fantasia_comercial,
                estado_establecimiento = estado_establecimiento,
                descripcion_provincia_est = descripcion_provincia_est,
                descripcion_canton_est = descripcion_canton_est,
                descripcion_parroquia_est = descripcion_parroquia_est,
                codigo_ciiu = codigo_ciiu,
                actividad_economica = actividad_economica
            )
            _sri_ente.save()
            columns = None


def cargar_info_csv(csv_file, user, separador):
    if csv_file:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(csv_file.read())
            file.close()

    with open(file=file.name, mode='r', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            #Lee información
            columns = ','.join(line).split(separador)
            ocid = columns[0]
            release_id = columns[1]
            sc_id = columns[2]
            awardID = columns[3]
            title = columns[4]
            description = columns[5]
            status = columns[6]
            contractPeriod_startDate = columns[7]
            contractPeriod_endDate = columns[8]
            contractPeriod_maxExtentDate = columns[9]
            contractPeriod_durationInDays = columns[10]
            amount = columns[11]
            currency = columns[12]
            dateSigned = columns[13]

            # Guarda solicitud de compra
            _solicitud_compra = solicitud_compra(
                ocid = ocid,
                release_id = release_id,
                sc_id = sc_id,
                awardID = awardID,
                title = title,
                description = description,
                status = status,
                contractPeriod_startDate = contractPeriod_startDate,
                contractPeriod_endDate = contractPeriod_endDate,
                contractPeriod_maxExtentDate = contractPeriod_maxExtentDate,
                contractPeriod_durationInDays = contractPeriod_durationInDays,
                amount = amount,
                currency = currency,
                dateSigned = dateSigned
            )
            _solicitud_compra.save()
            columns = None
