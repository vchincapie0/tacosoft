from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render

#Importacion modelos y formularios
from .models import MateriaPrima,Desinfeccion,CaracteristicasOrganolepticas,MateriaPrimaGenerica
from .forms import MateriaPrimaForm,CaracteristicasMPForm,CaracteristicasMPUpdateForm,DesinfeccionMPForm, DesinfeccionMPUpdateForm


# Create your views here.
class MateriaPrimaGenericaListView(LoginRequiredMixin, ListView):
    '''Clase para mostrar los datos de las materias primas'''
    model = MateriaPrimaGenerica
    template_name = "materiaprima/lista_mp_generica.html"
    login_url=reverse_lazy('users_app:login')
    paginate_by=10
    context_object_name = 'materiaprima'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        
        # Filtrar por nombre específico de la materia prima
        queryset = MateriaPrimaGenerica.objects.filter(
            mp_nombre__icontains=palabra_clave
        )
        
        return queryset


class MateriaPrimaListView(LoginRequiredMixin, ListView):
    '''Clase para mostrar los datos de las materias primas'''
    model = MateriaPrima
    template_name = "materiaprima/lista_mp.html"
    login_url=reverse_lazy('users_app:login')
    paginate_by=10
    context_object_name = 'materiaprima'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        
        # Filtrar por nombre específico de la materia prima
        queryset = MateriaPrima.objects.filter(
            mp_nombre__mp_nombre__icontains=palabra_clave
        ).prefetch_related('caracteristicasorganolepticas_set')
        
        return queryset

class MateriaPrimaCreateView(LoginRequiredMixin, CreateView):
    '''Clase donde se crea una nueva materia prima'''
    model = MateriaPrima
    template_name = "materiaprima/add_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = MateriaPrimaForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp') 

class CaracteristicasMateriaPrimaCreateView(LoginRequiredMixin, CreateView):
    '''Vista para la creacion de las caracteristicas organolepticas de la materia prima'''
    model = CaracteristicasOrganolepticas
    template_name = "materiaprima/caracteristicas_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = CaracteristicasMPForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp')
    
class CaracteristicasMateriaPrimaUpdateView(LoginRequiredMixin, UpdateView):
    '''Vista para la edicion de las caracteristicas organolepticas de la materia prima'''
    model = CaracteristicasOrganolepticas
    template_name = "materiaprima/updateCaracteristicas_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = CaracteristicasMPUpdateForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp')
    
class DesinfeccionMateriaPrimaCreateView(LoginRequiredMixin, CreateView):
    '''Vists para la creacion de la desinfeccion de la materia prima'''
    model = Desinfeccion
    template_name = "materiaprima/desinfeccion_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = DesinfeccionMPForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp')
    
    def form_valid(self, form):
        '''funcion para automatizar el campo '''
        user = self.request.user
             # Guarda el formulario sin commit para asignar manualmente el usuario
        desinfeccion = form.save(commit=False)
             # Asigna el usuario al campo pedi_user
        desinfeccion.responsable = user
             # Ahora sí, guarda el pedido en la base de datos
        desinfeccion.save()
        return super().form_valid(form)

class DesinfeccionMateriaPrimaUpdateView(LoginRequiredMixin, UpdateView):
    '''Vista para la edición de la desinfeccion de la materia prima'''
    model = Desinfeccion
    template_name = "materiaprima/updateDesinfeccion_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = DesinfeccionMPUpdateForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp')
    
class MateriaPrimaDetailView(LoginRequiredMixin, DetailView):
    '''Vista donde se muestran los detalles de la materia prima'''
    model = MateriaPrima
    template_name = "materiaprima/detail_mp.html"
    login_url=reverse_lazy('users_app:login')
    context_object_name = 'materiaprima'

    

