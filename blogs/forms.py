from django import forms
from blogs.models import Articulo, Comentario


class ArtForm(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['fecha', 'titulo', 'subtitulo', 'cuerpo', 'imagen']


class BuscarArtForm(forms.Form):
    titulo = forms.CharField(min_length=3, max_length=20)


class ComForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['date', 'titulo', 'comentar', 'articulo']






