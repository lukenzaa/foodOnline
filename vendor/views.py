from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages


def vprofile(request):
    return render(request, 'vendor/vprofile.html')
