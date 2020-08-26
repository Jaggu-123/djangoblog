from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
    url(r'^$', views.articles_list, name='list'),
    url(r'^create/$', views.articles_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.articles_detail, name='detail')
]