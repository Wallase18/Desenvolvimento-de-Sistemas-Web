from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.conf import settings
from django.contrib import messages
# Create your views here.

def Agenda(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))
    lista_de_contatos = Contatos.objects.all()
    Contexto = {
    "lista_de_contatos":lista_de_contatos,
    }
    return render(request,"aplicaçao/Agenda.html",Contexto)

@login_required
def criar_contato(request):
    form = FormContatos(request.POST or None)

    if form.is_valid():
        form.save()
        messages.info(request,'Contato criado com sucesso!')
        return redirect('Agenda')

    return render(request, 'aplicaçao/Contatos_form.html', {'form': form})

@login_required
def atualizar_Contato(request,id):
    contato = Contatos.objects.get(id=id)
    form = FormContatos(request.POST or None,instance = contato)

    if form.is_valid():
        form.save()
        messages.info(request,'Contato atualizado com sucesso!')
        return redirect('Agenda')

    return render(request, 'aplicaçao/Contatos_form.html', {'form': form, 'contato':contato })

def deletar_contato(request, id):
    contato = Contatos.objects.get(id=id)

    if request.method == 'POST':
        contato.delete()
        messages.info(request,'Contato deletado com sucesso!')

        return redirect('Agenda')

    return render(request, 'aplicaçao/delete-confirm.html', {'contato':contato})
