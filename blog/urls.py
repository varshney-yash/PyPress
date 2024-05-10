from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-blogs'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='blog-detail'),
    path('blog/new/', views.PostCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update/', views.PostUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-delete'),
    path('about/', views.about, name='blog-about')
]