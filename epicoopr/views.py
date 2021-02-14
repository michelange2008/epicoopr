from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.utils import timezone

from epicomm.models import COmmande

class IndexView(ListView):

    def get_queryset(self):
        return Commande.objects.all()
