from django.shortcuts import render
from .forms import Create
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
    form_class = Create
    template_name = 'signup.html'
    success_url = reverse_lazy('login')