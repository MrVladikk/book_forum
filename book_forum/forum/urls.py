from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('logout/',views.logout,name='logout'),
]