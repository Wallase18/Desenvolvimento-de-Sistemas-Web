from django.urls import path
from . import views
from django.conf.urls.static import static

from projeto import settings


urlpatterns = [
    path('', views.Manga, name='manga'),
    path('criar_manga', views.criar_manga, name='criar_manga'),
    path('comentario', views.comentario, name='comentario'),
    path('criar_comentario', views.criar_comentario, name='criar_comentario'),
    # path('update/manga/<int:id>/', views.atualizar_manga, name='atualizar_manga'),
    path('delete/manga/<int:id>/', views.deletar_manga, name='deletar_manga'),
    path('cadastro', views.register, name='cadastro'),
    path('login', views.login, name='login'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
