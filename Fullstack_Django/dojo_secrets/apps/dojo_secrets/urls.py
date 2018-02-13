from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^register$',views.register),
    url(r'^success$',views.success),
    url(r'^logout$',views.logout),
    url(r'^popular$',views.mostPopular),
    url(r'^login$',views.login),
    url(r'^secrets$',views.postSecret),
    url(r'^like/(?P<id>\d+)$',views.like),
    url(r'^unlike/(?P<id>\d+)$',views.unlike),
    url(r'^delete/(?P<id>\d+)$',views.deleteSecret),
]
