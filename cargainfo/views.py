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

from analizaproveedor.models import solicitud_compra, sri_ente

# Create your views here.
def CargaInfoView(request):
    template_name = "cargainfo/cargainfo.html"
    context = {}    

    if request.method == 'POST':
        #file_path = settings.MEDIA_URL  + request.FILES['archivo_csv'].name
        #file = request.FILES['archivo_csv']
        #shutil.copyfileobj(file, open(file_path, 'wb+'))
        csv_file = request.FILES['archivo_csv']#file_path
        if csv_file[:7] == "SRI_RUC":
            cargar_info_sri(csv_file,request.user)
        
        if csv_file[:7] == "awards_":
            cargar_info_csv(csv_file,request.user)   


    return render(request,template_name,context)

def cargar_info_sri (csv_file,user):
    pass

def cargar_info_csv(csv_file,user):
    # Abrir el archivo CSV
    file_name = csv_file.name
    with open(file_name, 'r') as file_name:
        reader = csv.reader(file_name)        
        # Saltar la cabecera
        next(reader)
        # Recorrer cada registro
        for line in reader:
            # Obtener los datos de la venta
            a = a + 1
            #Grabar información
            """
            cliente = line[0]
            subTotal = line[1]
            totalVenta = line[2]
            porcIva = line[3]
            totalIva = line[4]
            id = None
            # Crear una nueva venta
            venta = Venta(
                cliente_id=cliente,
                subTotal=subTotal,
                totalVenta=totalVenta,
                porcIva=porcIva,
                totalIva=totalIva,
                usuarioCreacion= user
            )
            venta.save()
            id = venta.id
            # Obtener los datos del detalle de venta
            cultivo = line[5]
            produccion = line[6]
            cantidad = line[7]
            precio = line[8]
            total = line[9]

            # Crear un nuevo detalle de venta
            detalle_venta = DetalleVenta(
                venta=venta,
                cultivo_id=cultivo,
                produccion_id=produccion,
                cantidad=cantidad,
                precio=precio,
                total=total,
                usuarioCreacion= user
            )
            detalle_venta.save()
            #detalle_venta.save(commit=True)
            # Actualizar el campo fechaVenta
            venta.fechaVenta = line[10]
            venta.save()"""

        