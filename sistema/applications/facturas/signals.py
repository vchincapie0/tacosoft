from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Facturas, IVA, FacturasAudit
import threading

@receiver(pre_save, sender=Facturas)
def calcular_total_factura(sender, instance, **kwargs):
    # Obtener el valor de IVA asociado a la factura
    iva_valor = instance.fac_iva.valor if instance.fac_iva else 0.0
    
    # Calcular el total como subtotal más IVA
    subtotal = instance.fac_subtotal
    total = subtotal+((subtotal * iva_valor)/100)  # Calcular el total con IVA
    # Asignar el total calculado a fac_total
    instance.fac_total = total

# Obtener el modelo de usuario personalizado
User = get_user_model()

@receiver(post_save, sender=Facturas)
def log_facturas_change(sender, instance, created, **kwargs):
    current_user = getattr(threading, 'current_user', None)

    if current_user:
        changed_by = current_user

    if instance.deleted:
        action = 'D'  # Marcar como eliminado
        details = f"{instance.num_factura} ha sido borrado."
    elif created:
        action = 'C'  # Creación de Pedidos
        details = f"{instance.num_factura} ha sido creado."
    else:
        action = 'U'  # Actualización de Pedidos
        details = f"La información de {instance.num_factura} ha sido actualizado."

    # Crear el registro de auditoría con el usuario que realizó la acción
    FacturasAudit.objects.create( changed_by=changed_by, pedido=instance.fac_numeroPedido, proveedor=instance.fac_proveedor, action=action, details=details)
