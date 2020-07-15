from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import Coalesce

from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .serializers import CounterItemSerializer
from .models import Counter, CounterItem


# ---------------------------------------------
# Template Views
# ---------------------------------------------

def page_counter(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    last_counter = Counter.objects.all().order_by('-date').first()

    stats = CounterItem.objects.filter(counter=last_counter).aggregate(total=Coalesce(Sum('count'), 0))
    return render(request, 'counter.html', locals())


# ---------------------------------------------
# API Views
# ---------------------------------------------

class CounterItemsModelViewSet(ModelViewSet):
    queryset = CounterItem.objects.all()
    serializer_class = CounterItemSerializer

    def perform_create(self, serializer):
        """ Override to set the last event (counter as default value) """
        last_counter = Counter.objects.all().order_by('-date').first()
        serializer.save(counter=last_counter)
