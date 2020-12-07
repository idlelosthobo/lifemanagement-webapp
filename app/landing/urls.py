from django.urls import path
from app.landing import views

urlpatterns = [
    path('', views.HomeDetailView.as_view(), name='home_detail_view'),
]
