from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'categorie']
        labels = {
            'titre': 'Titre',
            'contenu': 'Contenu',
            'categorie': 'Catégorie',
        } 