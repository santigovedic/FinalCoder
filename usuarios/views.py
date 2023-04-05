from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from usuarios.forms import UserRegisterForm, UserEditForm
from usuarios.models import Avatar


def login_user(request):  # Formulario de inicio de sesión.

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            info = form.cleaned_data
            user = authenticate(username=info["username"], password=info["password"])

            if user:
                login(request, user)
                # Ver si no le puedo meter un mensaje de exito o que directamente me muestre el avatar.
                return redirect("inicio")  # Todavia no se si quiero que me lleve al inicio o a la vista donde están todos los blogs, o a la de mi perfil.
            else:
                return redirect("inicio")  # Que me lleve a una vista donde no se haya encontrado el usuario. Y me permita de ahi registrarme o reintentar el inicio de sesion.

    form = AuthenticationForm()
    contexto = {"form": form}
    return render(request, "usuarios/login.html", context=contexto)


def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    form = UserRegisterForm()
    contexto = {"form": form}
    return render(request, "usuarios/registro.html", context=contexto)

@login_required
def editar_user(request):

    user = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES)

        if form.is_valid():
            informacion = form.cleaned_data

            user.username = informacion["username"]
            user.first_name = informacion["first_name"]
            user.last_name = informacion["last_name"]
            user.email = informacion["email"]

            try:
                user.avatar.imagen = informacion["imagen"]
                user.avatar.save()
            except:
                avatar = Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()

            user.save()
            return render(request, "base.html")

    form = UserEditForm(initial={
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    })

    context = {"form": form, "nombre": user.first_name}
    return render(request, "usuarios/edicion.html", context=context)



