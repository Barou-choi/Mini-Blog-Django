from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
    CATEGORIES = [
        ('django', 'Django'),
        ('python', 'Python'),
        ('actu', 'Actualités'),
    ]
    
    titre = models.CharField(max_length=200)
    contenu = RichTextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    date_creation = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre 