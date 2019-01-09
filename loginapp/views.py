from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #class base forms
from django.views.generic import CreateView
from django.urls import reverse_lazy
def home(request):
    return render(request,'home.html')

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

