from django.db import models
from applications.users.models import User
from applications.materiaprima.models import MateriaPrima
from applications.insumos.models import ImplementosTrabajo
from applications.proveedores.models import Proveedores
from django.utils import timezone

# Create your models here.

class Pedidos(models.Model):

    ESTADO_CHOICES=(
        ('0','Completo'),
        ('1','Incompleto'),
        ('2','Rechazado'),

    )

    id=models.AutoField('id',primary_key=True)
    ref_pedido=models.IntegerField('Referencia',unique=True)
    pedi_user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank= True)
    pedi_fecha=models.DateField('fecha',default=timezone.now)
    pedi_estado=models.CharField('estado',max_length=1, choices=ESTADO_CHOICES)
    pedi_comprobatePago=models.CharField('Comprobante Pago',max_length=45)
    pedi_proveedor=models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    pedi_materiaprima=models.ManyToManyField(MateriaPrima, blank=True)
    pedi_insumos=models.ManyToManyField(ImplementosTrabajo, blank=True)
    is_active = models.BooleanField(default=True)  # Campo para el borrado lógico

    def __str__(self):
        estado = dict(self.ESTADO_CHOICES)[self.pedi_estado] if self.pedi_estado else 'Estado Desconocido'
        return f"N° Pedido: {self.ref_pedido} - Estado: {estado}"

    def delete(self, using=None, keep_parents=False):
        '''Funcion para borrado lógico'''
        self.is_active = False  # Marcar como inactivo en lugar de eliminar
        self.save(using=using)



