from django.db import models

# Contrac
class contrato(models.Model): 
    ocid = models.CharField(max_length=260, null=True)
    lanzamiento_id = models.CharField(max_length=260, null=True)
    contrato_id = models.CharField(max_length=260, null=True)
    otorgamientoID = models.CharField(max_length=260, null=True)
    título = models.CharField(max_length=260, null=True)
    descripción = models.CharField(max_length=260, null=True)
    estado = models.CharField(max_length=260, null=True)
    fechaInicioPeriodoContrato = models.CharField(max_length=260, null=True)
    fechaFinPeriodoContrato = models.CharField(max_length=260, null=True)
    fechaMaximaPeriodoContrato = models.CharField(max_length=260, null=True)
    duracionEnDíasPeriodoContrato = models.CharField(max_length=260, null=True)
    monto = models.CharField(max_length=260, null=True)
    moneda = models.CharField(max_length=260, null=True)
    fechaFirma = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}: {}'.format(self.ocid, self.título)

    def save(self):
        self.ocid = self.ocid
        self.lanzamiento_id = self.lanzamiento_id
        self.contrato_id = self.contrato_id
        self.otorgamientoID = self.otorgamientoID
        self.título = self.título
        self.descripción = self.descripción
        self.estado = self.estado
        self.fechaInicioPeriodoContrato = self.fechaInicioPeriodoContrato
        self.fechaFinPeriodoContrato = self.fechaFinPeriodoContrato
        self.fechaMaximaPeriodoContrato = self.fechaMaximaPeriodoContrato
        self.duracionEnDíasPeriodoContrato = self.duracionEnDíasPeriodoContrato
        self.monto = self.monto
        self.moneda = self.moneda
        self.fechaFirma = self.fechaFirma
        super(contrato, self).save() 

    class Meta:
        verbose_name_plural = "contratos"
        db_table = 'contrato'

# Tender
class licitacion(models.Model): 
    ocid = models.CharField(max_length=260, null=True)
    lanzamiento_id = models.CharField(max_length=260, null=True)
    licitacion_id = models.CharField(max_length=260, null=True)
    título = models.CharField(max_length=260, null=True)
    descripción = models.CharField(max_length=260, null=True)
    estado = models.CharField(max_length=260, null=True)
    idEntidadCompradora = models.CharField(max_length=260, null=True)
    nombreEntidadCompradora = models.CharField(max_length=260, null=True)
    montoTotal = models.CharField(max_length=260, null=True)
    moneda = models.CharField(max_length=260, null=True)
    métodoAdquisición = models.CharField(max_length=260, null=True)
    detallesMétodoAdquisición = models.CharField(max_length=260, null=True)
    categoríaPrincipalAdquisición = models.CharField(max_length=260, null=True)
    criteriosAdjudicación = models.CharField(max_length=260, null=True)
    fechaInicioPeriodoLicitación = models.CharField(max_length=260, null=True)
    fechaFinPeriodoLicitación = models.CharField(max_length=260, null=True)
    fechaMaximaPeriodoLicitación = models.CharField(max_length=260, null=True)
    duracionEnDíasPeriodoLicitación = models.CharField(max_length=260, null=True)
    fechaInicioPeriodoConsulta = models.CharField(max_length=260, null=True)
    fechaFinPeriodoConsulta = models.CharField(max_length=260, null=True)
    fechaMaximaPeriodoConsulta = models.CharField(max_length=260, null=True)
    duracionEnDíasPeriodoConsulta = models.CharField(max_length=260, null=True)
    tieneConsultas = models.CharField(max_length=260, null=True)
    criteriosElegibilidad = models.CharField(max_length=260, null=True)
    fechaInicioPeriodoAdjudicación = models.CharField(max_length=260, null=True)
    fechaFinPeriodoAdjudicación = models.CharField(max_length=260, null=True)
    fechaMaximaPeriodoAdjudicación = models.CharField(max_length=260, null=True)
    duraciónEnDíasPeriodoAdjudicación = models.CharField(max_length=260, null=True)
    númeroDeOfertantes = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}: {}'.format(self.ocid, self.título)

    def save(self):
        self.ocid = self.ocid
        self.lanzamiento_id = self.lanzamiento_id
        self.licitacion_id = self.licitacion_id
        self.título = self.título
        self.descripción = self.descripción
        self.estado = self.estado
        self.idEntidadCompradora = self.idEntidadCompradora
        self.nombreEntidadCompradora = self.nombreEntidadCompradora
        self.montoTotal = self.montoTotal
        self.moneda = self.moneda
        self.métodoAdquisición = self.métodoAdquisición
        self.detallesMétodoAdquisición = self.detallesMétodoAdquisición
        self.categoríaPrincipalAdquisición = self.categoríaPrincipalAdquisición
        self.criteriosAdjudicación = self.criteriosAdjudicación
        self.fechaInicioPeriodoLicitación = self.fechaInicioPeriodoLicitación
        self.fechaFinPeriodoLicitación = self.fechaFinPeriodoLicitación
        self.fechaMaximaPeriodoLicitación = self.fechaMaximaPeriodoLicitación
        self.duracionEnDíasPeriodoLicitación = self.duracionEnDíasPeriodoLicitación
        self.fechaInicioPeriodoConsulta = self.fechaInicioPeriodoConsulta
        self.fechaFinPeriodoConsulta = self.fechaFinPeriodoConsulta
        self.fechaMaximaPeriodoConsulta = self.fechaMaximaPeriodoConsulta
        self.duracionEnDíasPeriodoConsulta = self.duracionEnDíasPeriodoConsulta
        self.tieneConsultas = self.tieneConsultas
        self.criteriosElegibilidad = self.criteriosElegibilidad
        self.fechaInicioPeriodoAdjudicación = self.fechaInicioPeriodoAdjudicación
        self.fechaFinPeriodoAdjudicación = self.fechaFinPeriodoAdjudicación
        self.fechaMaximaPeriodoAdjudicación = self.fechaMaximaPeriodoAdjudicación
        self.duraciónEnDíasPeriodoAdjudicación = self.duraciónEnDíasPeriodoAdjudicación
        self.númeroDeOfertantes = self.númeroDeOfertantes
        super(licitacion, self).save()

    class Meta:
        verbose_name_plural = "licitaciones"
        db_table = 'licitacion'

# supplier
class proveedor(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    lanzamiento_id = models.CharField(max_length=260, null=True)
    otorgamiento_id = models.CharField(max_length=260, null=True)
    proveedor_id = models.CharField(max_length=260, null=True)
    nombre = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}: {}'.format(self.ocid, self.nombre)

    def save(self):
        self.ocid = self.ocid
        self.lanzamiento_id = self.lanzamiento_id
        self.otorgamiento_id = self.otorgamiento_id
        self.proveedor_id = self.proveedor_id
        self.nombre = self.nombre
        super(proveedor, self).save()

    class Meta:
        verbose_name_plural = "proveedores"
        db_table = "proveedor"

#planning
class planificacion(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    planificacion = models.CharField(max_length=260, null=True)
    justificación = models.CharField(max_length=260, null=True)
    idPresupuesto = models.CharField(max_length=260, null=True)
    descripciónPresupuesto = models.CharField(max_length=260, null=True)
    montoPresupuesto = models.CharField(max_length=260, null=True)
    monedaPresupuesto = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}: {}'.format(self.ocid, self.descripciónPresupuesto)

    def save(self):
        self.ocid = self.ocid
        self.planificacion = self.planificacion
        self.justificación = self.justificación
        self.idPresupuesto = self.idPresupuesto
        self.descripciónPresupuesto = self.descripciónPresupuesto
        self.montoPresupuesto = self.montoPresupuesto
        self.monedaPresupuesto = self.monedaPresupuesto
        super(planificacion, self).save()
    
    class Meta:
        verbose_name_plural = "planificaciones"
        db_table = 'planificacion'

#release
class lanzamiento(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    lanzamiento_id = models.CharField(max_length=260, null=True)
    tipoInicio = models.CharField(max_length=260, null=True)
    idComprador = models.CharField(max_length=260, null=True)
    nombreComprador = models.CharField(max_length=260, null=True)
    idioma = models.CharField(max_length=260, null=True)
    fecha = models.CharField(max_length=260, null=True)
    etiqueta = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}: {}'.format(self.ocid, self.nombreComprador)
    
    def save(self):
        self.ocid = self.ocid
        self.lanzamiento_id = self.lanzamiento_id
        self.tipoInicio = self.tipoInicio
        self.idComprador = self.idComprador
        self.nombreComprador = self.nombreComprador
        self.idioma = self.idioma
        self.fecha = self.fecha
        self.etiqueta = self.etiqueta
        super(lanzamiento, self).save()

    class Meta:
        verbose_name_plural = "lanzamientos"
        db_table = 'lanzamiento'

#award
class otorgamiento(models.Model):
    ocid = models.CharField(max_length=260, null=True)
    lanzamiento_id = models.CharField(max_length=260, null=True)
    otorgamiento_id = models.CharField(max_length=260, null=True)
    título = models.CharField(max_length=260, null=True)
    descripción = models.CharField(max_length=260, null=True)
    estado = models.CharField(max_length=260, null=True)
    fecha = models.CharField(max_length=260, null=True)
    monto = models.CharField(max_length=260, null=True)
    moneda = models.CharField(max_length=260, null=True)
    montoCorregido = models.CharField(max_length=260, null=True)
    monedaCorregida = models.CharField(max_length=260, null=True)
    montoIngresado = models.CharField(max_length=260, null=True)
    monedaIngresada = models.CharField(max_length=260, null=True)
    fechaInicioPeriodoContrato = models.CharField(max_length=260, null=True)
    fechaFinPeriodoContrato = models.CharField(max_length=260, null=True)
    fechaMaximaPeriodoContrato = models.CharField(max_length=260, null=True)
    duracionEnDíasPeriodoContrato = models.CharField(max_length=260, null=True)

    def __str__(self):
        return '{}: {}'.format(self.ocid, self.descripción)

    def save(self):
        self.ocid = self.ocid
        self.lanzamiento_id = self.lanzamiento_id
        self.otorgamiento_id = self.otorgamiento_id
        self.título = self.título
        self.descripción = self.descripción
        self.estado = self.estado
        self.fecha = self.fecha
        self.monto = self.monto
        self.moneda = self.moneda
        self.montoCorregido = self.montoCorregido
        self.monedaCorregida = self.monedaCorregida
        self.montoIngresado = self.montoIngresado
        self.monedaIngresada = self.monedaIngresada
        self.fechaInicioPeriodoContrato = self.fechaInicioPeriodoContrato
        self.fechaFinPeriodoContrato = self.fechaFinPeriodoContrato
        self.fechaMaximaPeriodoContrato = self.fechaMaximaPeriodoContrato
        self.duracionEnDíasPeriodoContrato = self.duracionEnDíasPeriodoContrato
        super(otorgamiento, self).save()

    class Meta:
        verbose_name_plural = "otorgamientos"
        db_table = 'otorgamiento'