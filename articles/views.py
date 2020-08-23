from django.shortcuts import render
from .models import Articles

def articles_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/artcles_list.html', {'articles': articles})
