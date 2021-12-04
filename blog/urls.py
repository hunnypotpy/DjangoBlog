from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>', views.blog_detail, name='blog_detail'),
    path('new', views.blog_new, name='blog_new'),
    path('edit/<int:pk>', views.blog_edit, name='blog_edit'),
    path('delete/<int:pk>', views.blog_delete, name='blog_delete'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('upload/', views.image_upload_view)
]

#from corey:
'''from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]'''



