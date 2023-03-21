from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls import url
from django.contrib.auth import views as auth_views




urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('blog.urls')),
    # path('members/', include('django.contrib.auth.urls')),
    # path('members/', include('members.urls')),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='auth_login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(next_page='login'), name='auth_logout'),
    url(r'^accounts/password/change$', auth_views.PasswordChangeView.as_view (template_name='password_change.html',success_url=reverse_lazy('login')),name='auth_password_change'),


]
