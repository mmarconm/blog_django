from django.shortcuts import render, HttpResponse

# Create your views here.

def articles_list(request):
    return HttpResponse('<h1>Articles List</h1>')