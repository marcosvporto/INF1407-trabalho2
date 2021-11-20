from django.urls.conf import path
from clientes import views

app_name = "clientes"

urlpatterns = [
    path('lista/', views.ClientesListView.as_view(), name='lista-clientes'),
    path('', views.ClientesListView.as_view(), name='home-clientes'),
    path('cria/', views.ClienteCreateView.as_view(), name='cria-cliente'),
    path('atualiza/<int:pk>/', views.ClienteUpdateView.as_view(), name='atualiza-cliente'),
    path('apaga/<int:pk>/', views.ClienteDeleteView.as_view(), name='apaga-cliente'),
    path('planos/cria/', views.PlanoCreateView.as_view(), name='cria-plano')
]