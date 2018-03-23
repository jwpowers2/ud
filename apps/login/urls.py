from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logoff$', views.logoff),
    url(r'^signin/', views.signin),
    url(r'^register/', views.register),
    url(r'^enter/', views.enter),
    url(r'^create/', views.create)
]

