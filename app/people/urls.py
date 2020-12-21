from django.urls import path
from app.people import views

urlpatterns = [
    path('<int:pk>/form/', views.PeopleFormView.as_view(), name='people_form'),
    path('all/', views.PeopleListView.as_view(), name='people_list'),
]
