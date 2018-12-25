from django.conf.urls import url
from . import views

app_name = "crm"

urlpatterns = [

    url(r'(?P<id>\w+)/$', views.dashboard, name='dashboard'),


    ]