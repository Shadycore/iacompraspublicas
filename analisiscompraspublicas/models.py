from io import open_code
from unicodedata import name
from django.db import models

class contract(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    release_id = models.CharField(max_length=260, null=True)
    co_id = models.CharField(max_length=260, null=True)
    awardID = models.CharField(max_length=260, null=True)
    title = models.CharField(max_length=260, null=True)
    description = models.CharField(max_length=260, null=True)
    status = models.CharField(max_length=260, null=True)
    contractPeriod_startDate = models.CharField(max_length=260, null=True)
    contractPeriod_endDate = models.CharField(max_length=260, null=True)
    contractPeriod_maxExtentDate = models.CharField(max_length=260, null=True)
    contractPeriod_durationInDays = models.CharField(max_length=260, null=True)
    amount = models.CharField(max_length=260, null=True)
    currency = models.CharField(max_length=260, null=True)
    dateSigned = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}:{}'.format(self.ocid, self.title)

    def save(self):
        self.ocid = self.ocid
        self.release_id = self.release_id
        self.co_id = self.co_id
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
        super(contract, self).save() 

    class Meta:
        verbose_name_plural = "contracts"
        db_table = 'contract'


class tender(models.Model): 
    ocid = models.CharField(max_length=260, null=True)
    release_id = models.CharField(max_length=260, null=True)
    te_id = models.CharField(max_length=260, null=True)
    title = models.CharField(max_length=260, null=True)
    description = models.CharField(max_length=260, null=True)
    status = models.CharField(max_length=260, null=True)
    procuringEntity_id = models.CharField(max_length=260, null=True)
    procuringEntity_name = models.CharField(max_length=260, null=True)
    value_amount = models.CharField(max_length=260, null=True)
    value_currency = models.CharField(max_length=260, null=True)
    procurementMethod = models.CharField(max_length=260, null=True)
    procurementMethodDetails = models.CharField(max_length=260, null=True)
    mainProcurementCategory = models.CharField(max_length=260, null=True)
    awardCriteria = models.CharField(max_length=260, null=True)
    tenderPeriod_startDate = models.CharField(max_length=260, null=True)
    tenderPeriod_endDate = models.CharField(max_length=260, null=True)
    tenderPeriod_maxExtentDate = models.CharField(max_length=260, null=True)
    tenderPeriod_durationInDays = models.CharField(max_length=260, null=True)
    enquiryPeriod_startDate = models.CharField(max_length=260, null=True)
    enquiryPeriod_endDate = models.CharField(max_length=260, null=True)
    enquiryPeriod_maxExtentDate = models.CharField(max_length=260, null=True)
    enquiryPeriod_durationInDays = models.CharField(max_length=260, null=True)
    hasEnquiries = models.CharField(max_length=260, null=True)
    eligibilityCriteria = models.CharField(max_length=260, null=True)
    awardPeriod_startDate = models.CharField(max_length=260, null=True)
    awardPeriod_endDate = models.CharField(max_length=260, null=True)
    awardPeriod_maxExtentDate = models.CharField(max_length=260, null=True)
    awardPeriod_durationInDays = models.CharField(max_length=260, null=True)
    numberOfTenderers = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}:{}'.format(self.ocid, self.title)

    def save(self):
        self.ocid = self.ocid
        self.release_id = self.release_id
        self.id = self.id
        self.title = self.title
        self.description = self.description
        self.status = self.status
        self.procuringEntity_id = self.procuringEntity_id
        self.procuringEntity_name = self.procuringEntity_name
        self.value_amount = self.value_amount
        self.value_currency = self.value_currency
        self.procurementMethod = self.procurementMethod
        self.procurementMethodDetails = self.procurementMethodDetails
        self.mainProcurementCategory = self.mainProcurementCategory
        self.awardCriteria = self.awardCriteria
        self.tenderPeriod_startDate = self.tenderPeriod_startDate
        self.tenderPeriod_endDate = self.tenderPeriod_endDate
        self.tenderPeriod_maxExtentDate = self.tenderPeriod_maxExtentDate
        self.tenderPeriod_durationInDays = self.tenderPeriod_durationInDays
        self.enquiryPeriod_startDate = self.enquiryPeriod_startDate
        self.enquiryPeriod_endDate = self.enquiryPeriod_endDate
        self.enquiryPeriod_maxExtentDate = self.enquiryPeriod_maxExtentDate
        self.enquiryPeriod_durationInDays = self.enquiryPeriod_durationInDays
        self.hasEnquiries = self.hasEnquiries
        self.eligibilityCriteria = self.eligibilityCriteria
        self.awardPeriod_startDate = self.awardPeriod_startDate
        self.awardPeriod_endDate = self.awardPeriod_endDate
        self.awardPeriod_maxExtentDate = self.awardPeriod_maxExtentDate
        self.awardPeriod_durationInDays = self.awardPeriod_durationInDays
        self.numberOfTenderers = self.numberOfTenderers
        super(tender, self).save()

    class Meta:
        verbose_name_plural = "tenders"
        db_table = 'tender'


class supplier(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    release_id = models.CharField(max_length=260, null=True)
    award_id = models.CharField(max_length=260, null=True)
    su_id = models.CharField(max_length=260, null=True)
    name = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}:{}'.format(self.ocid, self.name)

    def save(self):
        self.ocid = self.ocid
        self.release_id = self.release_id
        self.award_id = self.award_id
        self.su_id = self.su_id
        self.name = self.name
        super(supplier, self).save()

    class Meta:
        verbose_name_plural = "suppliers"
        db_table = "supplier"


class planning(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    pa_id = models.CharField(max_length=260, null=True)
    rationale = models.CharField(max_length=260, null=True)
    budget_id = models.CharField(max_length=260, null=True)
    budget_description = models.CharField(max_length=260, null=True)
    budget_amount = models.CharField(max_length=260, null=True)
    budget_currency = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}:{}'.format(self.ocid, self.budget_description)

    def save(self):
        self.ocid = self.ocid
        self.pa_id = self.pa_id
        self.rationale = self.rationale
        self.budget_id = self.budget_id
        self.budget_description = self.budget_description
        self.budget_amount = self.budget_amount
        self.budget_currency = self.budget_currency
        super(planning, self).save()
    
    class Meta:
        verbose_name_plural = "plannings"
        db_table = 'planning'


class release(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    re_id = models.CharField(max_length=260, null=True)
    initiationType = models.CharField(max_length=260, null=True)
    buyer_id = models.CharField(max_length=260, null=True)
    buyer_name = models.CharField(max_length=260, null=True)
    language = models.CharField(max_length=260, null=True)
    date = models.CharField(max_length=260, null=True)
    tag = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}:{}'.format(self.ocid, self.buyer_name)
    
    def save(self):
        self.ocid = self.ocid
        self.re_id = self.re_id
        self.initiationType = self.initiationType
        self.buyer_id = self.buyer_id
        self.buyer_name = self.buyer_name
        self.language = self.language
        self.date = self.date
        self.tag = self.tag
        super(release, self).save()

    class Meta:
        verbose_name_plural = "releases"
        db_table = 'release'


class award(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    release_id = models.CharField(max_length=260, null=True)
    aw_id = models.CharField(max_length=260, null=True)
    title = models.CharField(max_length=260, null=True)
    description = models.CharField(max_length=260, null=True)
    status = models.CharField(max_length=260, null=True)
    date = models.CharField(max_length=260, null=True)
    amount = models.CharField(max_length=260, null=True)
    currency = models.CharField(max_length=260, null=True)
    correctedValue_amount = models.CharField(max_length=260, null=True)
    correctedValue_currency = models.CharField(max_length=260, null=True)
    enteredValue_amount = models.CharField(max_length=260, null=True)
    enteredValue_currency = models.CharField(max_length=260, null=True)
    contractPeriod_startDate = models.CharField(max_length=260, null=True)
    contractPeriod_endDate = models.CharField(max_length=260, null=True)
    contractPeriod_maxExtentDate = models.CharField(max_length=260, null=True)
    contractPeriod_durationInDays = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}:{}'.format(self.ocid, self.description)

    def save(self):
        self.ocid = self.ocid
        self.release_id = self.release_id
        self.aw_id = self.aw_id
        self.title = self.title
        self.description = self.description
        self.status = self.status
        self.date = self.date
        self.amount = self.amount
        self.currency = self.currency
        self.correctedValue_amount = self.correctedValue_amount
        self.correctedValue_currency = self.correctedValue_currency
        self.enteredValue_amount = self.enteredValue_amount
        self.enteredValue_currency = self.enteredValue_currency
        self.contractPeriod_startDate = self.contractPeriod_startDate
        self.contractPeriod_endDate = self.contractPeriod_endDate
        self.contractPeriod_maxExtentDate = self.contractPeriod_maxExtentDate
        self.contractPeriod_durationInDays = self.contractPeriod_durationInDays
        super(award, self).save()

    class Meta:
        verbose_name_plural = "awards"
        db_table = 'award'

class sri_ente(models.Model):
    numero_ruc = models.CharField(max_length=260)
    razon_social = models.CharField(max_length=260)
    provincia_jurisdiccion = models.CharField(max_length=260)
    nombre_comercial = models.CharField(max_length=260)
    estado_contribuyente = models.CharField(max_length=260)
    clase_contribuyente = models.CharField(max_length=260)
    fecha_inicio_actividades = models.DateField(blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)
    fecha_suspension_definitiva = models.DateField(blank=True, null=True)
    fecha_reinicio_actividades = models.DateField(blank=True, null=True)
    obligado = models.CharField(max_length=260)
    tipo_contribuyente = models.CharField(max_length=260)
    numero_establecimiento = models.CharField(max_length=260)
    nombre_fantasia_comercial = models.CharField(max_length=260)
    estado_establecimiento = models.CharField(max_length=260)
    descripcion_provincia_est = models.CharField(max_length=260)
    descripcion_canton_est = models.CharField(max_length=260)
    descripcion_parroquia_est = models.CharField(max_length=260)
    codigo_ciiu = models.CharField(max_length=260)
    actividad_economica = models.CharField(max_length=260)

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
