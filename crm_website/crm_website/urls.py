"""crm_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
import crm.views, general_customers.views, sentimental_analysis.views

app_name ='crm_website'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', crm.views.UserFormView.as_view(), name='post'),
    path('privacy/', crm.views.privacy, name='privacy'),
    url(r'timeline/', general_customers.views.timeline, name='timeline'),
    url(r'analysis/', sentimental_analysis.views.analysis, name='analysis'),
    path('crm/', include('crm.urls_crm')),
    url(r'gc/', include('general_customers.urls_gc')),
    url(r'email/', include('emails.urls_email')),
    url(r'refbonus/', include('refbonus.urls_ref'))
]
