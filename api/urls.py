from django.urls import path,include
from . import views
urlpatterns = [
    path("list-notes/", views.getAllNotes, name="list-notes"),
    path("detail-note/<int:pk>/", views.getNote, name="detail-note"),  
    path("create-note/", views.createNote, name="create-note"),
    path("update-note/<int:pk>/", views.updateNote, name="update-note"),
    path("delete-note/<int:pk>/", views.deleteNote, name="delete-note"),
]
