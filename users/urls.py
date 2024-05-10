from django.urls import path
from .views import register, logout_view, profile

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile')
]
