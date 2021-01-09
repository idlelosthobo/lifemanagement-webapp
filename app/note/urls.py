from django.urls import path
from app.note import views

urlpatterns = [
    path('<int:pk>/form/', views.NoteFormView.as_view(), name='note_form'),
    path('all/', views.NoteListView.as_view(), name='note_list'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
]
