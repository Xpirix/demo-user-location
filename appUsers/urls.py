from django.urls import path

from . import views

urlpatterns = [
    path('', views.users_map, name='users_map'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('register', views.signup, name='register'),
]