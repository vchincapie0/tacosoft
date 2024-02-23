import re
from django import forms
from .models import Pedidos
from applications.materiaprima.models import MateriaPrima
from applications.insumos.models import ImplementosTrabajo
from applications.proveedores.models import Proveedores

class PedidosCreateForm(forms.ModelForm):

    PEDIDO_CHOICES=(
        ('0','materia prima'),
        ('1','insumos'),
    )

    tipo_pedido=forms.CharField(
        label='Tipo de Pedido',
        required=True,
        max_length=1,
        widget=forms.RadioSelect(
            choices=PEDIDO_CHOICES
        ),
    )

    class Meta:

        model=Pedidos
        fields=(
            'ref_pedido',
            'pedi_user',
            'pedi_fecha',
            'pedi_estado',
            'pedi_comprobatePago',
            'pedi_proveedor',
            'pedi_materiaprima',
            'pedi_insumos',
        )

        widgets={
            'ref_pedido':forms.NumberInput(attrs={'placeholder': 'Referencia del pedido'}),
            'pedi_fecha':forms.SelectDateWidget(),
            'pedi_comprobatePago':forms.TextInput(attrs={'placeholder':'Comprobante de Pago'}),
            'pedi_proveedor':forms.Select(),
            'pedi_materiaprima':forms.SelectMultiple(),
            'pedi_insumos':forms.SelectMultiple(),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Disable Insumos field initially
        #self.fields['pedi_insumos'].disabled = True

        # Add JavaScript event handler to toggle the disabled state
        self.fields['tipo_pedido'].widget.attrs['onchange'] = (
            'toggleInsumosField(this.value);'
        )

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.7.1.min.js',
        )

class PedidosUpdateForm(forms.ModelForm):

    PEDIDO_CHOICES=(
        ('0','materia prima'),
        ('1','insumos'),
    )

    tipo_pedido=forms.CharField(
        label='Tipo de Pedido',
        required=True,
        max_length=1,
        widget=forms.Select(
            choices=PEDIDO_CHOICES
        ),
    )

    class Meta:

        model=Pedidos
        fields=(
            'ref_pedido',
            'pedi_user',
            'pedi_fecha',
            'pedi_estado',
            'pedi_comprobatePago',
            'pedi_proveedor',
            'pedi_materiaprima',
            'pedi_insumos',
        )

        widgets={
            'ref_pedido':forms.NumberInput(attrs={'placeholder': 'Referencia del pedido'}),
            'pedi_fecha':forms.DateInput(),
            'pedi_comprobatePago':forms.TextInput(attrs={'placeholder':'Comprobante de Pago'}),
            'pedi_proveedor':forms.Select(),
            'pedi_materiaprima':forms.SelectMultiple(),
            'pedi_insumos':forms.SelectMultiple(),

        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Disable Insumos field initially
        #self.fields['pedi_insumos'].disabled = True

        # Add JavaScript event handler to toggle the disabled state
        self.fields['tipo_pedido'].widget.attrs['onchange'] = (
            'toggleInsumosField(this.value);'
        )

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.7.1.min.js',
        )

class PedidosAddMpCreateFrom(forms.ModelForm):
    """Form definition para crear materia prima en el formulario de pedidos."""

    class Meta:
        """Meta definition for MateriaPrimaform."""

        model = MateriaPrima
        fields = (
            'mp_lote',
            'mp_nombre',
            'mp_tipo',
            'mp_cantidad',
            'mp_fechallegada',
            'mp_fechavencimiento',
            )
        
        widgets={
            'mp_nombre':forms.TextInput(attrs={'placeholder': 'Nombre Materia Prima'}),
            'mp_fechallegada':forms.SelectDateWidget(),
            'mp_fechavencimiento':forms.SelectDateWidget(),
        }
    
    def clean_it_cantidad(self):
        cantidad = self.cleaned_data['it_cantidad']
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser un número mayor que 0.")
        return cantidad

class PedidosAddInsumosCreateFrom(forms.ModelForm):
    """Form definition Implementos de Trabajo en pedidos."""

    class Meta:
        """Meta definition for implementosTrabajoform."""

        model = ImplementosTrabajo
        fields = (
            'it_codigo',
            'it_nombre',
            'it_cantidad',
            'it_fechaEntrega',
            'it_estado',
            )
        
        widgets={
            'it_nombre':forms.TextInput(attrs={'placeholder': 'Nombre del Implemento'}),
            'it_cantidad':forms.NumberInput(attrs={'placeholder': 'Cantidad Entregada'}),
            'it_fechaEntrega':forms.SelectDateWidget(),
        }

    def clean_it_cantidad(self):
        cantidad = self.cleaned_data['it_cantidad']
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser un número mayor que 0.")
        return cantidad
    
    def clean_it_nombre(self):
        nombre = self.cleaned_data['it_nombre']
        if not re.match("^[a-zA-Z ]+$", nombre):
            raise forms.ValidationError("El nombre no debe contener números o caracteres especiales.")
        return nombre

class  PedidosAddProveedorCreateFrom(forms.ModelForm):
    """Form definition Proveedores."""
    class Meta:

        model=Proveedores
        fields=(
            'nit',
            'prov_nombre',
            'prov_telefono',
        )

        widgets={
            'prov_nombre':forms.TextInput(attrs={'placeholder': 'Nombre del Implemento'}),
            'prov_telefono':forms.TextInput(attrs={'placeholder': 'Teléfono', 'type':'number'}),
        }

    def clean_prov_telefono(self):
        cantidad = self.cleaned_data['prov_telefono']
        if len(cantidad) < 10:
            raise forms.ValidationError("El teléfono debe tener al menos 10 digitos.")
        return cantidad
    
    def clean_prov_nombre(self):
        nombre = self.cleaned_data['prov_nombre']
        if not re.match("^[a-zA-Z ]+$", nombre):
            raise forms.ValidationError("El nombre no debe contener números o caracteres especiales.")
        return nombre