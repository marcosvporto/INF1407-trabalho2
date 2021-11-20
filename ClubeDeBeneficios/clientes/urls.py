from django.urls.conf import path
from clientes import views

app_name = "clientes"

urlpatterns = [
    path('lista/', views.ClientesListView.as_view(), name='lista-clientes'),
    path('', views.ClientesListView.as_view(), name='home-clientes'),
    path('cria/', views.ClienteCreateView.as_view(), name='cria-cliente'),
    path('atualiza/<int:pk>/', views.ClienteUpdateView.as_view(), name='atualiza-cliente'),
    path('apaga/<int:pk>/', views.ClienteDeleteView.as_view(), name='apaga-cliente'),
    
    path('planos/cria/', views.PlanoCreateView.as_view(), name='cria-plano'),
    path('planos/lista/', views.PlanosListView.as_view(), name='lista-planos'),
    path('planos/atualiza/<int:pk>/', views.PlanoUpdateView.as_view(), name='atualiza-plano'),
    path('planos/apaga/<int:pk>/', views.PlanoDeleteView.as_view(), name='apaga-plano'),
    
    path('consultas/cria/', views.ConsultaCreateView.as_view(), name='cria-consulta'),
    path('consultas/lista/', views.ConsultaListView.as_view(), name='lista-consultas'),
    path('consultas/atualiza/<int:pk>/', views.ConsultaUpdateView.as_view(), name='atualiza-consulta'),
    path('consultas/apaga/<int:pk>/', views.ConsultaDeleteView.as_view(), name='apaga-consulta'),

]