from django.urls import path

from . import views

urlpatterns = [
    path(r'^formpage/', views.example,name="example")
]