from django.urls.conf import path
from clientes import views

app_name = "clientes"

urlpatterns = [
    path('lista/', views.ClientesListView.as_view(), name='lista-clientes'),
    path('', views.ClientesListView.as_view(), name='home-clientes')

]