from django.urls import path
from . import views

urlpatterns = [
  path("", views.index),
  path("create/", views.create),
  path("read/", views.read),
  path("main/", views.main),
  path("sub/", views.sub),
  path("three/", views.three),
  path("four/", views.four),
  path("delete/", views.delete)
]