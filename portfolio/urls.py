from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('wordpress/', views.wordpress, name='wordpress'),
]
