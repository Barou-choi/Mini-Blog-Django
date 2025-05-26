from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

def accueil(request):
    articles = Article.objects.all()
    return render(request, 'articles/accueil.html', {'articles': articles})

def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/detail_article.html', {'article': article})

@login_required
def creer_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.save()
            messages.success(request, 'Article créé avec succès!')
            return redirect('accueil')
    else:
        form = ArticleForm()
    return render(request, 'articles/creer_article.html', {'form': form})

@login_required
def supprimer_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.auteur:
        article.delete()
        messages.success(request, 'Article supprimé avec succès!')
    else:
        messages.error(request, 'Vous n\'avez pas la permission de supprimer cet article.')
    return redirect('accueil') 