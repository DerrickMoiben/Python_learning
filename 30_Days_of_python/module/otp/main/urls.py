from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('all_users/', views.all_users, name='all_users'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('verifyotp/', views.verifyotp, name='verifyotp'),
    path('verifyotp/', views.verifyotp, name='verifyotp'),    
]