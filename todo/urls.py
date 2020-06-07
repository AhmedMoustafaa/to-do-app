from django.urls import path
from .views import todo_list, update_item, delete_item
urlpatterns = [
    path('', todo_list, name='home'),
    path('update/<str:pk>/', update_item, name='update'),
    path('delete/<str:pk>/', delete_item, name='delete'),
]