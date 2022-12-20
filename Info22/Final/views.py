from django.shortcuts import render
from App.noticias.forms import ContactoForm
# Create your views here.
def Index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def password(request):
    return render(request, 'password.html')

def donaciones(request):
    return render(request, 'donaciones.html')

#-----View de la pág con el formulario para contactos:
def Contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
#-----

