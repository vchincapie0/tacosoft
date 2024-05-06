from django.urls import path
from . import views

app_name='procesamientos_app'

urlpatterns = [
    path('procesamientos/',views.ProcesamientosView.as_view(),name='procesamientos'),
    path('picado/',views.PicadoListView.as_view(),name='picado'),
    path('add_picado/',views.PicadocreateView.as_view(),name='add_picado'),
    path('delete_picado/<pk>',views.PicadoDeleteView.as_view(),name='delete_picado'),
    path('update_picado/<pk>',views.PicadoUpdateView.as_view(),name='update_picado'),
    path('coccion/',views.CoccionListView.as_view(),name='coccion'),
    path('add_coccion/',views.CoccioncreateView.as_view(),name='add_coccion'),
    path('delete_coccion/<pk>',views.CoccionDeleteView.as_view(),name='delete_coccion'),
    path('equipos/',views.EquiposListView.as_view(),name='equipos'),
    path('add_equipos/',views.EquiposcreateView.as_view(),name='add_equipos'),
    path('delete_equipo/<pk>',views.EquiposDeleteView.as_view(),name='delete_equipo'),
]