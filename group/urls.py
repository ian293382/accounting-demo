from django.urls import path

from . import views

app_name = 'group'

urlpatterns = [
    path('', views.groups, name='groups'),
    path('new/', views.new_group, name='new'),
    path('<int:pk>/', views.detail, name='detail'),

    path('<int:pk>/delete/', views.delete_group, name='delete'),
    path('<int:pk>/edit/', views.edit_group, name='edit'),
]