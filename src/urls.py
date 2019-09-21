from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('accounts/password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('accounts/password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('accounts/change-password/',auth_views.PasswordChangeView.as_view(template_name=
    'users/change_password.html', success_url='/accounts/change-password/done/'),name='change_password'),
    path('accounts/change-password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'),name='change_password_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
