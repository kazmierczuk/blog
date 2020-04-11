from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('new_post/', views.new_post_view, name='new_post'),
    path('list/', views.PostListView.as_view(), name='list'),
    path('list/<int:pk>/', views.PostDetailView.as_view(), name='read_post'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
]
