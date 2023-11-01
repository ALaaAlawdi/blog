from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_post, name='all_post'),
    path('<int:id>/', views.post, name='post'),
    path('create/', views.create_post, name='create_post'),
    path('<int:id>/edit/', views.edit_post, name='edit_post'),
]
