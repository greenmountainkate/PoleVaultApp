from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    url(r'^athlete/(?P<pk>\d+)/$', views.athlete, name='athlete'),
    url(r'^session/(?P<pk>\d+)/$', views.session, name='session'),
    path('athletes/', views.athletes, name='athletes'),
    path('sessions/', views.sessions, name='sessions'),
    path('calibrate', views.calibrate, name='calibrate'),
]
