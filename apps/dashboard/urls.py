
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', views.admin),
    url(r'^decision/', views.decision),
    url(r'^logoff/', views.logoff)
]

