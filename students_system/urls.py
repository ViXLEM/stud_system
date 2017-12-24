from django.conf.urls import url

from . import views

app_name = 'students_system'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^facultet/(?P<name>\w+)/$', views.facultet, name='facultet'),
    url(r'^group/(?P<name>\w+)/$', views.group, name='group'),
    url(r'^facultets_list/$', views.fc_list, name='facultet_list'),
] 
