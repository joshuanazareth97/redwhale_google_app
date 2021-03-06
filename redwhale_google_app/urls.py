"""redwhale_google_app URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import google_auth.views as rw_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace="google")),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', rw_views.logout_view, name='logout'),
    path('', rw_views.homepage, name='homepage'),
    path('edit_profile', rw_views.edit_profile, name='edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
