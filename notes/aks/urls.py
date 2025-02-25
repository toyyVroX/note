from django.urls import path
from aks.views import note_create, note_list, note_detail, note_delete

app_name = 'aks'

urlpatterns = [
    path("note_list", note_list, name='note_list'),
    path('note_detail/<int:pk>/', note_detail, name='note_detail'),
    path("note_create/", note_create, name='note_create'),
    path('note_delete/<int:pk>/delete/', note_delete, name='note_delete'),
]