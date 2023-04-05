from django.urls import path
from usuarios.views import login_user, registro, editar_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_user, name="login"),
    path('signup/', registro, name="signup"),
    path('logout/', LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"), # Todavia no se como funciona porque no me meti con login.
    path('editar/', editar_user, name="editar"),
]