from django.urls import path

from .views import (
  BlogListView,
  BlogDetailView,
  BlogCreateView,
  BlogUpdateView,
  BlogDeleteView,
)

urlpatterns = [
  path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='postDelete'),
  path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='postEdit'),
  path('post/new/', BlogCreateView.as_view(), name='postNew'),
  path('post/<int:pk>/', BlogDetailView.as_view(), name='postDetail'),
  path('', BlogListView.as_view(), name='home')
]
