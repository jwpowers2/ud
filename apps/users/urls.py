from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/', views.new),
    url(r'^edit_user/(?P<id_to_edit>\d+)/', views.edit_user),
    url(r'^update_user/(?P<id_to_update>\d+)/', views.update_user),
    url(r'^show_profile/(?P<profile_id>\d+)/', views.show_profile),
    url(r'^admin_edit_user/(?P<id_to_edit>\d+)/', views.admin_edit_user),
    url(r'^logoff/', views.logoff),
    url(r'^show/(?P<id>\d+)/', views.show),
    url(r'^(?P<id>\d+)/create_message', views.create_message),
    url(r'^create_comment/(?P<messageid>\d+)/(?P<userid>\d+)/', views.create_comment),
    url(r'^decision/(?P<id_to_edit>\d+)/', views.decision),
    url(r'^remove_user/(?P<id>\d+)/', views.remove_user),
]

