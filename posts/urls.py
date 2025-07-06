from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/new/', views.new_post, name='new_post'),
    path('admin-panel/delete/<int:post_id>', views.delete_post, name='delete_post'),
    path('', views.post_list, name='post_list')
]