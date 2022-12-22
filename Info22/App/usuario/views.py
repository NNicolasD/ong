from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .models import Usuario
from .forms import RegistroUsuarioForm,UserCreationForm

class RegistrarUsuario(CreateView):
    model         = Usuario
    form_class    = RegistroUsuarioForm
    template_name = 'log/register.html'
    success_url   = reverse_lazy('App.usuario:login')

def Usuarios(request):
    usuarios = Usuario.objects.all()
    context={
        'usuarios': usuarios,
    }
    return render(request,'usuario/listarUsuarios.html', context)

class DeleteUsuario(DeleteView):
    model           = Usuario
    template_name = 'usuario/usuario_delete.html'
    success_url   = reverse_lazy('App.usuario:listarUsuarios')