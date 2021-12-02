from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('tools/', views.tools_index, name='tools_index'),
  path('tools/<int:tool_id>/', views.tools_detail, name='tools_detail'),
  path('tools/create/', views.toolCreate.as_view(), name='tools_create'),
  path('tools/<int:pk>/update/', views.toolUpdate.as_view(), name='tools_update'),
  path('tools/<int:pk>/delete/', views.toolDelete.as_view(), name='tools_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]