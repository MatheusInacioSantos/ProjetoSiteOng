from django.shortcuts import render, redirect
from app.forms import CadastroForm, ContatoForm
from app.models import Cadastro, Contato
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        all = data['db'] = Cadastro.objects.filter(situacao__icontains=search)
    else:
        all = data['db'] = Cadastro.objects.all()
    paginator = Paginator(all, 9)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CadastroForm()
    return render(request, 'form.html', data)

def contato(request):
    data = {}
    data['form'] = ContatoForm()
    return render(request, 'contato.html', data)

def info(request):
    return render(request, 'info.html')

def cadastro(request):
    data = {}
    search = request.GET.get('search')
    if search:
        all = data['db'] = Cadastro.objects.filter(nome__icontains=search)
    else:
        all = data['db'] = Cadastro.objects.all()
    paginator = Paginator(all, 9)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'cadastro.html', data)

def solicitacoes(request):
    data = {}
    search = request.GET.get('search')
    if search:
        all = data['db'] = Contato.objects.filter(nome__icontains=search)
    else:
        all = data['db'] = Contato.objects.all()
    paginator = Paginator(all, 5)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'solicitacoes.html', data)

def create(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def createcontato(request):
    formcontato = ContatoForm(request.POST or None)
    if formcontato.is_valid():
        formcontato.save()
        return redirect('solicitacoes')

def view(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    return render(request, 'view.html', data)

def viewContato(request, pk):
    data = {}
    data['db'] = Contato.objects.get(pk=pk)
    return render(request, 'viewContato.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    data['form'] = CadastroForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Cadastro.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Cadastro.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def deleteContato(request, pk):
    db = Contato.objects.get(pk=pk)
    db.delete()
    return redirect('solicitacoes')