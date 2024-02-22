from django.urls import path
from . import views

app_name='pedidos_app'

urlpatterns = [
    path('list_pedidos/',views.PedidosListView.as_view(),name='list_pedidos'),
]