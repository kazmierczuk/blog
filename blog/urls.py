from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('new_post', views.new_post_view, name='new_post'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='read_post'),
]
