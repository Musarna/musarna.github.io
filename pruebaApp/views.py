from django.shortcuts import render, redirect, get_object_or_404
from pruebaApp.forms import JugueteForm,LibroForm,RopaForm
from pruebaApp.models import Juguete,Libro,Ropa
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def inicio(request):
    data = {}
    return render(request, "pruebaApp/inicio.html",data)


@permission_required('pruebaApp.add_juguete')
def crear_juguete(request):
    if request.method == "POST":
        form = JugueteForm(request.POST, request.FILES)
        if form.is_valid():
            codigo_producto = form.cleaned_data['codigoProducto']
            # Verificar si ya existe un juguete con el mismo código de producto
            if Juguete.objects.filter(codigoProducto=codigo_producto).exists():
                form.add_error('codigoProducto', 'Este código de producto ya existe.')
            else:
                form.save()
                messages.success(request, "Juguete creado exitosamente.")
                return redirect('/juguetes')
    else:
        form = JugueteForm()

    return render(request, "pruebaApp/juguete.html", {'form': form})

def mostrar_juguetes(request):
    query = request.GET.get('q', '')  # Obtener la búsqueda desde la URL, o vacío si no hay búsqueda
    if query:
        # Filtrar los juguetes por el nombre que comience con el término de búsqueda
        juguetes = Juguete.objects.filter(nombre__icontains=query)  # 'icontains' es case-insensitive
    else:
        juguetes = Juguete.objects.all()  # Si no hay búsqueda, mostramos todos

    data = {'juguetes': juguetes, 'query': query}
    return render(request, "pruebaApp/juguetes.html", data)


def juguete_detalles(request, id):
    # Obtener el producto según su ID
    juguete = get_object_or_404(Juguete, id=id)
    return render(request, 'pruebaApp/juguete_detalles.html', {'juguete': juguete})

    
    # Pasar el producto a la plantilla  

@permission_required('pruebaApp.change_juguete')
def cargar_editar_juguetes(request, juguete_id):
    juguete = get_object_or_404(Juguete,id=juguete_id)
    form = JugueteForm(instance=juguete)
    data = {"form":form, 'juguete':juguete}

    return render(request, "pruebaApp/jugueteEditar.html",data)

@permission_required('pruebaApp.change_juguete')
def editar_juguete(request, juguete_id):
    juguete = get_object_or_404(Juguete, id=juguete_id)

    if request.method == "POST":
        form = JugueteForm(request.POST, request.FILES, instance=juguete)
        if form.is_valid():
            nuevo_codigo = form.cleaned_data['codigoProducto']
            # Verificar si el nuevo código de producto ya existe en otro juguete
            if Juguete.objects.filter(codigoProducto=nuevo_codigo).exclude(id=juguete_id).exists():
                form.add_error('codigoProducto', 'Este código de producto ya existe.')
            else:
                if 'foto' in request.FILES:
                    juguete.foto = request.FILES["foto"]
                form.save()
                return redirect("/juguetes/")
    else:
        form = JugueteForm(instance=juguete)

    return render(request, "pruebaApp/jugueteEditar.html", {'form': form, 'juguete': juguete})


@permission_required('pruebaApp.delete_juguete')
def eliminar_juguete(request, juguete_id):
    juguete = get_object_or_404(Juguete,id=juguete_id)
    if request.method == "POST":
        juguete.delete()
        return redirect ("/juguetes/")
    
    return render(request, "pruebaApp/jugueteDel.html",{"juguete":juguete})


def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario en la base de datos
            messages.success(request, 'Cuenta creada con éxito. Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirige al login después de registrarse
    else:
        form = UserCreationForm()
    
    return render(request, 'pruebaApp/registro.html', {'form': form})