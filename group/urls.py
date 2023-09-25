from django.urls import path

from . import views

from financialtrack import views as financialtrack_views

app_name = 'group'

urlpatterns = [
    path('', views.groups, name='groups'),
    path('new/', views.new_group, name='new'),
    path('<int:pk>/', views.detail, name='detail'),

    path('<int:pk>/delete', views.delete_group, name='delete'),
    path('<int:group_pk>/edit/', views.edit_group, name='edit'),

    path('<int:pk>/financial_records/new', financialtrack_views.new_financial_record, name='new_record'),
    path('<int:pk>/financial_records/<int:record_pk>/edit/', financialtrack_views.edit_financial_record, name='edit_record'),
    path('<int:pk>/financial_records/<int:record_pk>/delete/', financialtrack_views.delete_financial_record, name='delete_record'),

    path('<int:pk>/tags/new', financialtrack_views.new_tag, name='new_tag'),
    path('<int:pk>/tags/<int:tag_pk>/edit/', financialtrack_views.edit_tag, name='edit_tag'),
    path('<int:pk>/tags/<int:tag_pk>/delete/', financialtrack_views.delete_tag, name='delete_tag'),
]