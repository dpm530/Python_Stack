from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^about$',views.about),
    url(r'^project$',views.project),
    url(r'^testimonial$',views.testimonial),
    url(r'^$',views.index),
]
