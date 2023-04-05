from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from usuarios.forms import UserRegisterForm, UserEditForm
from usuarios.models import Avatar
from django.contrib import messages


def login_user(request):  # Vista del LOG IN --> Para que el usuario inicie sesión.

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            info = form.cleaned_data
            user = authenticate(username=info["username"], password=info["password"])

            if user:
                login(request, user)
                return redirect("inicio")
        else:
            messages.warning(request, "El usuario o la contraseña son incorrectos.")

    form = AuthenticationForm()
    contexto = {"form": form}
    return render(request, "usuarios/login.html", context=contexto)


def registro(request):  # Vista de SIGN UP --> Para que un usuario se registre.
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.warning(request, "No se pudo registrar el usuario.")

    form = UserRegisterForm()
    contexto = {"form": form}
    return render(request, "usuarios/registro.html", context=contexto)


@login_required
def editar_user(request):  # Vista para que un usuario edite su perfil. Si o si debe de estar logueado.

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
        else:
            messages.warning(request, "No se pudo editar el usuario.")

    form = UserEditForm(initial={
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    })

    context = {"form": form, "nombre": user.first_name}
    return render(request, "usuarios/edicion.html", context=context)



