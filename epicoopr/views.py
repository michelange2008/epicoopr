from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.utils import timezone


def index(request):
    return render(request, 'index.html')
