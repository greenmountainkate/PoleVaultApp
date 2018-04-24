from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    url(r'^athlete/(?P<pk>\d+)/$', views.athlete, name='athlete'),
]
