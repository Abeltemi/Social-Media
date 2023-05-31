from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name="logout"),
    path('', views.index, name="index"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user/password_change.html'), name="password_change"),
    path('pasword_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'), name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"), name="password_reset"),
    path('password_reset_confirm', auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_done.html'), name="passwowrd_reset_done"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name="password_reset_complete"),
    path('register/', views.register,name='register'),
    path('profile', views.profile, name='profile'), 
    path('profile/edit', views.edit, name='edit'),
]