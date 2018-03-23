from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/', views.new),
    url(r'^edit/$', views.edit),
    url(r'^edit/(?P<id>\d+)/', views.edituser),
    url(r'^logoff/', views.logoff),
    url(r'^show/(?P<id>\d+)/', views.show),
    url(r'^(?P<id>\d+)/create_message', views.create_message),
    url(r'^create_comment/(?P<messageid>\d+)/(?P<userid>\d+)/', views.create_comment),
]

