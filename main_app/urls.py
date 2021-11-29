from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tools/', views.tools_index, name='tools_index'),
  path('tools/<int:tool_id>/', views.tools_detail, name='tools_detail'),
  path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
]