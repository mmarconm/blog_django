from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator

# Local imports
from articles.models import Article


def articles_list(request):
    articles = Article.objects.all().order_by('-published_at')
    paginator = Paginator(articles, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'articles/articles_list.html', {'page_obj': page_obj})

    # return render(request, 'articles/articles_list.html',
    #               {'articles': articles, 'title': 'Articles Blog Post'})
