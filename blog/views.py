from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post

# Create your views here.
class BlogListView(ListView):
  model = Post
  template_name = 'home.html'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'postDetail.html'

class BlogCreateView(CreateView):
  model = Post
  template_name = 'postNew.html'
  fields = ['title', 'author', 'body']
