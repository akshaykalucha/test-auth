
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.htm'), name='login'),
    #path('logout/', views.logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.htm'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]