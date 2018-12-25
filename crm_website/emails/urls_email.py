from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.emailcompose, name='emailcompose'),
    url(r'^send/$', views.sendmail,name='sendmail'),
    url(r'^read/$', views.readmail,name='readmail'),
    url(r'^emailread/$', views.emailread, name='emailread'),
]