from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'counter.html', locals())