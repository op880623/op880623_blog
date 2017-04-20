from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='article list'),
    # url(r'^article/$', views.article_content),
    url(r'^(?P<id>[0-9]+)/$', views.article_content),
]
