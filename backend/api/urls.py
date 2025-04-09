from django.urls import path
from . import views

urlpatters = [
    path('summary/', views.summary)
]