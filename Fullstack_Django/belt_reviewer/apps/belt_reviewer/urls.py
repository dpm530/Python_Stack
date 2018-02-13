from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^success$',views.success),
    url(r'^login$',views.login),
    url(r'^createWindow$',views.createWindow),
    url(r'^createNewBook$',views.createNewBook),
    url(r'^newBook/(?P<book_id>\d+)$',views.newBook),
    url(r'^delete/(?P<review_id>\d+)$',views.deleteReview),
]
