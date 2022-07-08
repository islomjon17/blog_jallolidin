from django.urls import path
from .views import SignUpView, UserEditView, ChangePasswordView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', ChangePasswordView.as_view(
        template_name='registration/change-password.html')),
    path('password_success', views.password_success, name='password_success')
]
