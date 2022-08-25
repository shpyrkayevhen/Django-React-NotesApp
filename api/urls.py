from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRouts, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/create/', views.createNote, name='note-create'),
    path('notes/<str:pk>/', views.get_update_delete_Note, name='note'),
]
