from django import forms
from . import models

class CreateArticle(forms.ModelForm):

    #define quais campos de modelos a minha aplicação vai utilizar
    class Meta:
        model = models.Article
        fields = [
            'title',
            'body',
            'slug',
            'thumb'
        ]
