from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from spectech.models import Technic

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^catalog/$',
        ListView.as_view(queryset=Technic.objects.all().order_by("name"),
        template_name="web/catalog.html")),
    path('create/', views.createTech),
    path('', views.getTech),
    path('catalog/delete/<int:id>/', views.delete),
    path('catalog/edit/<int:id>/', views.edit),
]