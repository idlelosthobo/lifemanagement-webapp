from django.urls import path
from app.core import views

urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
]
