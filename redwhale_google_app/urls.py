"""redwhale_google_app URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import .views as rw_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('google_auth/', include('social_django.urls', namespace="google")),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('', rw_views.homepage, name='homepage')
]
