"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatterns = [
    path('', views.index, name='css_index'),
    path('no_explicit_style', views.simple_table_without_explicit_style,
         name='simple_table_without_explicit_style'),
    path('with_template_in_table_class',
         views.no_template_in_table_class,
         name='no_template_in_table_class'),
    path('extends_built_in',
         views.extends_built_in,
         name='extends_built_in')
]
