from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('photos/upload/', views.upload_photo, name='upload_photo'),
    path('photos/list/', views.list_photos, name='list_photos'),
]

