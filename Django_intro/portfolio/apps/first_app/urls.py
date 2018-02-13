from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^testimonial$',views.testimonial),
    url(r'^$',views.index),
]
