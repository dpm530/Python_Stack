from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^userDashboard$',views.userDashboard),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^newUser$',views.newUser),
    url(r'^newReview$',views.newReview),
    url(r'^createNewBook$',views.createNewBook),
    url(r'^book/(?P<book_id>\d+)$',views.book),
    url(r'^delete/(?P<review_id>\d+)$',views.deleteReview),
]
