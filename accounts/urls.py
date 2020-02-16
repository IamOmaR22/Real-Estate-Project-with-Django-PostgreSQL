from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),   ## accounts/login (accounts come from main urls.py)
    path('register', views.register, name='register'),  ## accounts/register
    path('logout', views.logout, name='logout'),        ## accounts/logout
    path('dashboard', views.dashboard, name='dashboard'),   ## accounts/dashboard
]