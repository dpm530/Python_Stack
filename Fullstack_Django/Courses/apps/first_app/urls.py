from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^posts$',views.post),
    url(r'^confirm/(?P<id>\d+)$',views.confirm),
    url(r'^confirm/delete/(?P<id>\d+)$',views.delete)
]
