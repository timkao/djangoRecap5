from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
  path('post/new', BlogCreateView.as_view(), name='postNew'),
  path('post/<int:pk>', BlogDetailView.as_view(), name='postDetail'),
  path('', BlogListView.as_view(), name='home')
]
