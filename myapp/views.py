from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from .models import MyBase
# Create your views here.

def index(request):
    if request.GET and request.GET['username'] and request.GET['password']:
        if request.GET['username'] == 'admin' and request.GET['password'] == 'admin':
            print('!!!!!!!!!!!!!!!!!')
            return redirect('/myadmin/')
    
    return render(request, 'reg.html')


class HomeView(ListView):
    model = MyBase
    template_name = "index.html"


class AdminView(ListView):
    model = MyBase
    template_name = "admin.html"


class Add(CreateView):
    model = MyBase
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/myadmin/'


class Update(UpdateView):
    model = MyBase
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/myadmin/'


class Delete(DeleteView):
    model = MyBase
    template_name = 'delete.html'
    success_url = '/myadmin/'

