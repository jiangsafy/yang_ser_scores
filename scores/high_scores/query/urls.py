from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    url('^/link', views.get_top_n_users),
    # url('^/interval', views.get_top_interval),

]