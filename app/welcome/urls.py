from django.contrib import admin
from app.welcome import views
from django.urls import path, include

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
]
