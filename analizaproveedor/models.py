from io import open_code
from unicodedata import name
from django.db import models


class solicitud_compra(models.Model):
    ocid = models.CharField(max_length=250)
    release_id = models.CharField(max_length=250)
    sc_id = models.CharField(max_length=250)
    awardID = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    contractPeriod_startDate = models.DateField(blank=True, null=True)
    contractPeriod_endDate = models.DateField(blank=True, null=True)
    contractPeriod_maxExtentDate = models.CharField(max_length=250)
    contractPeriod_durationInDays = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    currency = models.CharField(max_length=250)
    dateSigned = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}:{}'.format(self.ocid, self.title)

    def save(self):
        self.ocid = self.ocid
        self.release_id = self.release_id
        self.sc_id = self.sc_id
        self.awardID = self.awardID
        self.title = self.title
        self.description = self.description
        self.status = self.status
        self.contractPeriod_startDate = self.contractPeriod_startDate
        self.contractPeriod_endDate = self.contractPeriod_endDate
        self.contractPeriod_maxExtentDate = self.contractPeriod_maxExtentDate
        self.contractPeriod_durationInDays = self.contractPeriod_durationInDays
        self.amount = self.amount
        self.currency = self.currency
        self.dateSigned = self.dateSigned
        super(solicitud_compra, self).save() 

    class Meta:
        verbose_name_plural = "solicitud_compras"
        db_table = 'solicitud_compra'


class sri_ente(models.Model):
    numero_ruc = models.CharField(max_length=250)
    razon_social = models.CharField(max_length=250)
    provincia_jurisdiccion = models.CharField(max_length=250)
    nombre_comercial = models.CharField(max_length=250)
    estado_contribuyente = models.CharField(max_length=250)
    clase_contribuyente = models.CharField(max_length=250)
    fecha_inicio_actividades = models.DateField(blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    fecha_suspension_definitiva = models.DateField(blank=True, null=True)
    fecha_reinicio_actividades = models.DateField(blank=True, null=True)
    obligado = models.CharField(max_length=250)
    tipo_contribuyente = models.CharField(max_length=250)
    numero_establecimiento = models.CharField(max_length=250)
    nombre_fantasia_comercial = models.CharField(max_length=250)
    estado_establecimiento = models.CharField(max_length=250)
    descripcion_provincia_est = models.CharField(max_length=250)
    descripcion_canton_est = models.CharField(max_length=250)
    descripcion_parroquia_est = models.CharField(max_length=250)
    codigo_ciiu = models.CharField(max_length=250)
    actividad_economica = models.CharField(max_length=250)

    def __str__(self):
        return '{}:{}'.format(self.nombre, self.lote)

    def save(self):
        self.numero_ruc = self.numero_ruc
        self.razon_social = self.razon_social
        self.provincia_jurisdiccion = self.provincia_jurisdiccion
        self.nombre_comercial = self.nombre_comercial
        self.estado_contribuyente = self.estado_contribuyente
        self.clase_contribuyente = self.clase_contribuyente
        self.fecha_inicio_actividades = self.fecha_inicio_actividades
        self.fecha_actualizacion = self.fecha_actualizacion
        self.fecha_suspension_definitiva = self.fecha_suspension_definitiva
        self.fecha_reinicio_actividades = self.fecha_reinicio_actividades
        self.obligado = self.obligado
        self.tipo_contribuyente = self.tipo_contribuyente
        self.numero_establecimiento = self.numero_establecimiento
        self.nombre_fantasia_comercial = self.nombre_fantasia_comercial
        self.estado_establecimiento = self.estado_establecimiento
        self.descripcion_provincia_est = self.descripcion_provincia_est
        self.descripcion_canton_est = self.descripcion_canton_est
        self.descripcion_parroquia_est = self.descripcion_parroquia_est
        self.codigo_ciiu = self.codigo_ciiu
        self.actividad_economica = self.actividad_economica 
        super(sri_ente, self).save()

    class Meta:
        verbose_name_plural = "sri_entes"
        db_table = 'sri_ente'
