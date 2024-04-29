from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save_audio, name='save_audio'),
    path('test/', views.test, name='test'),
]
