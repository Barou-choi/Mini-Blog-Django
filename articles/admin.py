from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date_creation')
    list_filter = ('categorie', 'auteur', 'date_creation')
    search_fields = ('titre', 'contenu')
    date_hierarchy = 'date_creation' 