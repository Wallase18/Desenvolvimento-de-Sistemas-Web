from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.conf import settings
from django.contrib import messages
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.
def Manga(request):
     if not request.user.is_authenticated:
         return redirect('login')

    lista_de_mangas = manga.objects.all()
    return render(request,"polls/mangas.html",{"lista_de_mangas":lista_de_mangas})

 @login_required
def comentario(request):
    lista_de_Comentario = Comentario.objects.all()
    return render(request,"polls/comentarios.html",{"lista_de_Comentario":lista_de_Comentario})

 @login_required
def criar_manga(request):
    form = FormManga(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('manga')
    else:
        form = FormManga()
    return render(request, 'polls/manga_form.html', {'form': form})

 @login_required
def criar_comentario(request):
    form = FormComentario(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('comentario')

    return render(request, 'polls/comentario_form.html', {'form': form})

# def atualizar_manga(request,id):
#     Manga = manga.objects.get(id=id)
#     form = FormManga(request.POST , request.FILES,instance = Manga)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('manga')
#     else:
#         form = FormManga()
#     return render(request, 'manga_form.html', {'form': form, 'Manga':Manga })
 @login_required
def deletar_manga(request, id):
    Manga = manga.objects.get(id=id)

    if request.method == 'POST':
        Manga.delete()
        # messages.info(request,'Contato deletado com sucesso!')

        return redirect('manga')

    return render(request, 'polls/delete-confirm.html', {'Manga':Manga})


def register(request):
    form = Formregister()
    if request.method == "POST":

        form = Formregister(data=request.POST)

        if form.is_valid():

            user = form.save()
            if user is not None:

                do_login(request, user)

                return redirect('login')

    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    return render(request, "registration/register.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('manga')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/login.html", {'form': form})
