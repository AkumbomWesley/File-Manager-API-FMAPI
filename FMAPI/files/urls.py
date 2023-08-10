from django.urls import path
from .views import get_all_files, get_file_by_id, update_file, delete_file, create_file, delete_all_files

urlpatterns = [
    path('files/', get_all_files, name='get_all_files'),
    path('files/<int:file_id>/', get_file_by_id, name='get_file_by_id'),
    path('files/<int:file_id>/update/', update_file, name='update_file'),
    path('files/<int:file_id>/delete/', delete_file, name='delete_file'),
    path('files/delete/', delete_all_files, name='delete_all_files'),
    path('files/create/', create_file, name='create_file'),
]