from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index_view, name="index"),
]
