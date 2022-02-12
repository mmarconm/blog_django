from django.shortcuts import render, HttpResponse

# Local imports
from articles.models import Article
# Create your views here.

def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles_list.html', {'articles': articles, 'title': 'Articles Blog Post'})