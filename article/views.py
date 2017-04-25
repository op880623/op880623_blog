from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from .models import Article, Classification
from django.http import HttpResponse


def list(request, page='1'):
    return HttpResponse("article list page")

def list_by_category(request, category=''):
    classification = Classification.objects.get(name=category)
    articles = get_list_or_404(Article, classification=classification)
    return render(request, 'startbootstrap-blog-4-dev/article.html')

def article_by_id(request, id):
    article = get_object_or_404(Article, id=int(id))
    return redirect(reverse('url_with_id_slug_category', kwargs={'id': str(int(id)).zfill(5), 'slug': article.slug(), 'category': article.classification.format_url()[:-1]}))

def article_by_category_id_slug(request, id, slug='', category=''):
    article = get_object_or_404(Article, id=int(id))
    if slug == article.slug() and id == str(int(id)).zfill(5) and category == article.classification.format_url()[:-1]:
        return render(request, 'startbootstrap-blog-4-dev/article.html',  {'article': article})
    else:
        return redirect(reverse('url_with_id', kwargs={'id': str(int(id)).zfill(5)}))
