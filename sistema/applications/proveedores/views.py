from django.http import HttpResponse
from openpyxl import Workbook
import csv
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Importacion de modelos y formularios
from .models import Proveedores, ProveedoresAudit
from .forms import ProveedorCreateForm, ProveedoresUpdateForm, ProveedorAuditFilterForm

class ProveedoresListView(LoginRequiredMixin, ListView):
    '''Clase para mostrar los datos de los proveedores'''
    model = Proveedores
    template_name = "proveedores/list_proveedor.html"
    login_url=reverse_lazy('users_app:login')
    paginate_by=10
    context_object_name = 'proveedor'

    def get_queryset(self):
        '''Funcion que toma de la barra de busqueda la pablabra clave para filtrar'''
        palabra_clave= self.request.GET.get("kword",'')
        lista = Proveedores.objects.filter(
            prov_nombre__icontains = palabra_clave,
            deleted=False  # Solo proveedores activos
        )
        return lista
    
class ProveedoresCreateView(LoginRequiredMixin,CreateView):
    '''Clase para crear nuevos proveedores'''
    model = Proveedores
    template_name = "proveedores/add_proveedor.html"
    login_url=reverse_lazy('home_app:home')
    #Campos que se van a mostrar en el formulario
    form_class = ProveedorCreateForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('proveedores_app:list_proveedores') 

class ProveedorUpdateView(LoginRequiredMixin, UpdateView):
    '''Vista para actualizar los datos de proveedores'''
    model = Proveedores
    template_name = "proveedores/edit_proveedor.html"
    login_url=reverse_lazy('users_app:login')
    form_class=ProveedoresUpdateForm
    success_url= reverse_lazy('proveedores_app:list_proveedores')

class ProveedoresDeleteView(LoginRequiredMixin, DeleteView):
    '''Vista para borrar Proveedores'''
    model = Proveedores
    template_name = "proveedores/delete_proveedor.html"
    login_url=reverse_lazy('users_app:login')
    success_url= reverse_lazy('proveedores_app:list_proveedores')

class ProveedoresAuditListView(LoginRequiredMixin, ListView):
    '''Clase para mostrar los datos de logs de proveedores'''
    model = ProveedoresAudit
    template_name = "administrador/auditorias/proveedoraudit.html"
    login_url=reverse_lazy('users_app:login')
    paginate_by=10
    context_object_name = 'proveedor'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener los parámetros de filtrado del formulario
        form = ProveedorAuditFilterForm(self.request.GET)

        # Aplicar filtros si el formulario es válido
        if form.is_valid():
            proveedor = form.cleaned_data.get('proveedor')
            action = form.cleaned_data.get('action')
            changed_by = form.cleaned_data.get('changed_by')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            # Filtrar por usuario, acción, usuario que realizó el cambio y rango de fechas
            if proveedor:
                queryset = queryset.filter(proveedor=proveedor)
            if action:
                queryset = queryset.filter(action=action)
            if changed_by:
                queryset = queryset.filter(changed_by=changed_by)
            if start_date:
                queryset = queryset.filter(changed_at__gte=start_date)
            if end_date:
                # Agregar 1 día a la fecha final para incluir todos los registros de ese día
                end_date += timezone.timedelta(days=1)
                queryset = queryset.filter(changed_at__lt=end_date)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ProveedorAuditFilterForm(self.request.GET)
        return context
    
def export_proveedores_to_excel(request):
    # Obtener los datos de proveedores que quieres exportar
    proveedores = Proveedores.objects.filter(deleted=False)  # Filtrar proveedores activos

    # Crear un nuevo libro de Excel y una hoja de trabajo
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'Proveedores'

    # Agregar encabezados a la primera fila
    worksheet.append(['NIT', 'Razón Social', 'Teléfono'])

    # Agregar datos de proveedores a las siguientes filas
    for proveedor in proveedores:
        worksheet.append([proveedor.nit, proveedor.prov_nombre, proveedor.prov_telefono])

    # Crear una respuesta HTTP con el archivo Excel como contenido
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=proveedores.xlsx'

    # Guardar el libro de Excel en la respuesta HTTP
    workbook.save(response)

    return response

def export_proveedores_to_csv(request):
    proveedores = Proveedores.objects.filter(deleted=False)  # Obtener datos de proveedores
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=proveedores.csv'

    writer = csv.writer(response)
    writer.writerow(['NIT', 'Razón Social', 'Teléfono'])  # Encabezados de columnas

    for proveedor in proveedores:
        writer.writerow([proveedor.nit, proveedor.prov_nombre, proveedor.prov_telefono])

    return response