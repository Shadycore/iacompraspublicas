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

from analisiscompraspublicas.models import contract, sri_ente, award, release, planning, supplier, tender


def CargaInfoView(request):
    template_name = "cargainfo/cargainfo.html"
    context = {}    

    if request.method == 'POST':
        csv_file = request.FILES['archivo_csv']
        # validar el nombre del archivo en los primeros 7 caracteres
        if csv_file.name[:10] == "contracts_":
            cargar_info_csv(csv_file, request.user, "|")

        if csv_file.name[:7] == "awards_":
            cargar_info_award(csv_file, request.user, "|")

        if csv_file.name[:9] == "releases_":
            cargar_info_release(csv_file, request.user, "|")

        if csv_file.name[:9] == "planning_":
            cargar_info_planning(csv_file, request.user, "|")

        if csv_file.name[:10] == "suppliers_":
            cargar_info_supplier(csv_file, request.user, "|")

        if csv_file.name[:7] == "tender_":
            cargar_info_tender(csv_file, request.user, "|")

        if csv_file.name[:7] == "SRI_RUC":
            cargar_info_sri(csv_file, request.user, "|")
        
    return render(request, template_name, context = { 'mensaje' : "Archivo procesado" })


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
            
            try:
                columns = ','.join(line).split(separador)
                ocid = columns[0] #.replace("'","")
                release_id = columns[1] #.replace("'","")
                co_id = columns[2] #.replace("'","")
                awardID = columns[3] #.replace("'","")
                title = columns[4] #.replace("'","")
                description = columns[5] #.replace("'","")
                status = columns[6] #.replace("'","")
                contractPeriod_startDate = columns[7][:10] # #.replace("'","")[:10]
                contractPeriod_endDate = columns[8] #.replace("'","")
                contractPeriod_maxExtentDate = columns[9] #.replace("'","")
                contractPeriod_durationInDays = columns[10] #.replace("'","")
                amount = columns[11] #.replace("'","")
                currency = columns[12] #.replace("'","")
                dateSigned = columns[13][:10] # #.replace("'","")[:10]

                # Guarda solicitud de compra
                ocontract = contract(
                    ocid = ocid,
                    release_id = release_id,
                    co_id = co_id,
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
                    dateSigned = dateSigned)
                ocontract.save()
            except Exception as e:
                columns = None
            finally:
                columns = None


def cargar_info_sri (csv_file, user, separador):
    if csv_file:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(csv_file.read())
            file.close()

    with open(file=file.name, mode='r', encoding="ansi") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            #Lee información
            try:
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
                osri_ente = sri_ente(
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
                osri_ente.save()
            except Exception as e:
                columns = None
            finally:
                columns = None


def cargar_info_award(csv_file, user, separador):
    if csv_file:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(csv_file.read())
            file.close()

    with open(file=file.name, mode='r', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            #Lee información
            try:
                columns = ','.join(line).split(separador)
                ocid = columns[0] #.replace("'","")
                release_id = columns[1] #.replace("'","")
                aw_id = columns[2] #.replace("'","")
                title = columns[3] #.replace("'","")
                description = columns[4] #.replace("'","")
                status = columns[5] #.replace("'","")
                date = columns[6] #.replace("'","")
                amount = columns[7] #.replace("'","")
                currency = columns[8] #.replace("'","")
                correctedValue_amount = columns[9] #.replace("'","")
                correctedValue_currency = columns[10] #.replace("'","")
                enteredValue_amount = columns[11] #.replace("'","")
                enteredValue_currency = columns[12] #.replace("'","")
                contractPeriod_startDate = columns[13][:10] # #.replace("'","")[:10]
                contractPeriod_endDate = columns[14][:10] # #.replace("'","")[:10]
                contractPeriod_maxExtentDate = columns[15][:10] # #.replace("'","")[:10]
                contractPeriod_durationInDays = columns[16] #.replace("'","")

                # Guarda solicitud de compra
                oaward = award(
                        ocid = ocid,
                        release_id = release_id,
                        aw_id = aw_id,
                        title = title,
                        description = description,
                        status = status,
                        date = date,
                        amount = amount,
                        currency = currency,
                        correctedValue_amount = correctedValue_amount,
                        correctedValue_currency = correctedValue_currency,
                        enteredValue_amount = enteredValue_amount,
                        enteredValue_currency = enteredValue_currency,
                        contractPeriod_startDate = contractPeriod_startDate,
                        contractPeriod_endDate = contractPeriod_endDate,
                        contractPeriod_maxExtentDate = contractPeriod_maxExtentDate,
                        contractPeriod_durationInDays = contractPeriod_durationInDays
                        )
                oaward.save()
            except Exception as e:
                columns = None
            finally:
                columns = None


def cargar_info_release(csv_file, user, separador):
    if csv_file:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(csv_file.read())
            file.close()

    with open(file=file.name, mode='r', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            #Lee información
            try:
                columns = ','.join(line).split(separador)
                ocid = columns[0] #.replace("'","")
                re_id = columns[1] #.replace("'","")
                initiationType = columns[2] #.replace("'","")
                buyer_id = columns[3] #.replace("'","")
                buyer_name = columns[4] #.replace("'","")
                language = columns[5] #.replace("'","")
                date = columns[6] #.replace("'","")
                tag = columns[7] #.replace("'","")

                # Guarda solicitud de compra
                orelease = release(
                        ocid = ocid,
                        re_id = re_id,
                        initiationType = initiationType,
                        buyer_id = buyer_id,
                        buyer_name = buyer_name,
                        language = language,
                        date = date,
                        tag = tag
                        )
                orelease.save()
            except Exception as e:
                columns = None
            finally:
                columns = None

def cargar_info_planning(csv_file, user, separador):
    if csv_file:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(csv_file.read())
            file.close()

    with open(file=file.name, mode='r', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            #Lee información
            try:
                columns = ','.join(line).split(separador)
                ocid = columns[0] #.replace("'","")
                pa_id = columns[1] #.replace("'","")
                rationale = columns[2] #.replace("'","")
                budget_id = columns[3] #.replace("'","")
                budget_description = columns[4] #.replace("'","")
                budget_amount = columns[5] #.replace("'","")
                budget_currency = columns[6] #.replace("'","")


                # Guarda solicitud de compra
                oplanning = planning(
                        ocid = ocid,
                        pa_id = pa_id,
                        rationale = rationale,
                        budget_id = budget_id,
                        budget_description = budget_description,
                        budget_amount = budget_amount,
                        budget_currency = budget_currency
                        )
                
                oplanning.save()
            except Exception as e:
                columns = None
            finally:
                columns = None

def cargar_info_supplier(csv_file, user, separador):
    if csv_file:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(csv_file.read())
            file.close()

    with open(file=file.name, mode='r', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            #Lee información
            try:
                columns = ','.join(line).split(separador)
                ocid = columns[0] #.replace("'","")
                release_id = columns[1] #.replace("'","")
                award_id = columns[2] #.replace("'","")
                su_id = columns[3] #.replace("'","")
                name = columns[4] #.replace("'","")

                # Guarda solicitud de compra
                osupplier = supplier(
                            ocid = ocid,
                            release_id = release_id,
                            award_id = award_id,
                            su_id = su_id,
                            name = name
                        )
                
                osupplier.save()
            except Exception as e:
                columns = None
            finally:
                columns = None

def cargar_info_tender(csv_file, user, separador):
    if csv_file:
        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(csv_file.read())
            file.close()

    with open(file=file.name, mode='r', encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            #Lee información
            try:
                columns = ','.join(line).split(separador)
                ocid = columns[0] #.replace("'","")
                release_id = columns[1] #.replace("'","")
                te_id = columns[2] #.replace("'","")
                title = columns[3] #.replace("'","")
                description = columns[4] #.replace("'","")
                status = columns[5] #.replace("'","")
                procuringEntity_id = columns[6] #.replace("'","")
                procuringEntity_name = columns[7] #.replace("'","")
                value_amount = columns[8] #.replace("'","")
                value_currency = columns[9] #.replace("'","")
                procurementMethod = columns[10] #.replace("'","")
                procurementMethodDetails = columns[11] #.replace("'","")
                mainProcurementCategory = columns[12] #.replace("'","")
                awardCriteria = columns[13] #.replace("'","")
                tenderPeriod_startDate = columns[14][:10] # #.replace("'","")[:10]
                tenderPeriod_endDate = columns[15][:10] # #.replace("'","")[:10]
                tenderPeriod_maxExtentDate = columns[16] #.replace("'","")
                tenderPeriod_durationInDays = columns[17] #.replace("'","")
                enquiryPeriod_startDate = columns[18][:10] # #.replace("'","")[:10]
                enquiryPeriod_endDate = columns[19][:10] # #.replace("'","")[:10]
                enquiryPeriod_maxExtentDate = columns[20][:10] # #.replace("'","")[:10]
                enquiryPeriod_durationInDays = columns[21] #.replace("'","")
                hasEnquiries = columns[22] #.replace("'","")
                eligibilityCriteria = columns[23] #.replace("'","")
                awardPeriod_startDate = columns[24][:10] # #.replace("'","")[:10]
                awardPeriod_endDate = columns[25][:10] # #.replace("'","")[:10]
                awardPeriod_maxExtentDate = columns[26][:10] # #.replace("'","")[:10]
                awardPeriod_durationInDays = columns[27] #.replace("'","")
                numberOfTenderers = columns[28] #.replace("'","")

                # Guarda solicitud de compra
                otender = tender(
                        ocid = ocid,
                        release_id = release_id,
                        te_id = te_id,
                        title = title,
                        description = description,
                        status = status,
                        procuringEntity_id = procuringEntity_id,
                        procuringEntity_name = procuringEntity_name,
                        value_amount = value_amount,
                        value_currency = value_currency,
                        procurementMethod = procurementMethod,
                        procurementMethodDetails = procurementMethodDetails,
                        mainProcurementCategory = mainProcurementCategory,
                        awardCriteria = awardCriteria,
                        tenderPeriod_startDate = tenderPeriod_startDate,
                        tenderPeriod_endDate = tenderPeriod_endDate,
                        tenderPeriod_maxExtentDate = tenderPeriod_maxExtentDate,
                        tenderPeriod_durationInDays = tenderPeriod_durationInDays,
                        enquiryPeriod_startDate = enquiryPeriod_startDate,
                        enquiryPeriod_endDate = enquiryPeriod_endDate,
                        enquiryPeriod_maxExtentDate = enquiryPeriod_maxExtentDate,
                        enquiryPeriod_durationInDays = enquiryPeriod_durationInDays,
                        hasEnquiries = hasEnquiries,
                        eligibilityCriteria = eligibilityCriteria,
                        awardPeriod_startDate = awardPeriod_startDate,
                        awardPeriod_endDate = awardPeriod_endDate,
                        awardPeriod_maxExtentDate = awardPeriod_maxExtentDate,
                        awardPeriod_durationInDays = awardPeriod_durationInDays,
                        numberOfTenderers = numberOfTenderers
                        )
                otender.save()
            except Exception as e:
                columns = None
            finally:
                columns = None