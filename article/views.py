from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def index(request):
    return HttpResponse("You're looking at question.")


def article_content(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'startbootstrap-blog-4-dev/post.html')
