from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'(?P<id>\w+)/$', views.g_customers, name='g_customers'),

]