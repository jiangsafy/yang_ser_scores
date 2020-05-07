from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    url('/upload$', views.post_top_n_users),

]