from django.conf.urls import patterns, url

from recipe import views

urlpatterns = patterns('',
    url(r'^display/', views.display, name='display'),
)
