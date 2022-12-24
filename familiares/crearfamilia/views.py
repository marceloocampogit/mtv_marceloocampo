from django.shortcuts import render
from django.http import HttpResponse, Http404

from crearfamilia.models import Familiar
# Create your views here.

def base(request):
    return render(request, "base.html", context = {})

def home(request):
    return render(request, "home.html", context = {})

def alta_familiar(request):
    new_fam1 = Familiar.objects.create(
        name = 'Juan',
        surname = 'Perez',
        age = 30,
        birthday = '1992-01-01'
    )

    new_fam2 = Familiar.objects.create(
        name = 'Diego',
        surname = 'Perez',
        age = 20,
        birthday = '2002-01-01'
    )

    new_fam3 = Familiar.objects.create(
        name = 'Martin',
        surname = 'Perez',
        age = 10,
        birthday = '2012-01-01'
    )
    return render(request, "familiares.html", context = {})

def leer_familia(request):

    familia = Familiar.objects.all().values()
    context = {
        'Familia': familia
    }
    return render(request, "familia.html", context = context)

def datos_familiar(request, id_familiar):
    try:
        familiar = Familiar.objects.get(id = id_familiar)
    except Familiar.DoesNotExist:
        raise Http404('No existe el familiar buscado')
    return render(request, 'familiar.html', {
        'familiar': familiar,
    })