from django.urls import path
from . import views


urlpatterns = [
    path('', views.Agenda, name='Agenda'),
    path('cadastro-de-Contatos',views.criar_contato,name='criar_contato'),
    path('update/Contatos/<int:id>/', views.atualizar_Contato, name='atualizar_Contato'),
    path('delete/Contatos/<int:id>/', views.deletar_contato, name='deletar_contato'),
]
