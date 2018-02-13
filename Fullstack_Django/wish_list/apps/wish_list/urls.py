from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^homePage$',views.homePage),
    url(r'^login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^addItemPage$',views.addItemPage),
    url(r'^addItem$',views.addItem),
    url(r'^deleteItem/(?P<item_id>\d+)$',views.deleteItem),
    url(r'^removeItem/(?P<item_id>\d+)$',views.removeItem),
    url(r'^addItem/(?P<item_id>\d+)$',views.addItem),
    url(r'^item/(?P<id>\d+)$',views.item),
]
