from django.urls import path
from api.views import register_view, example_view
from rest_framework.authtoken.views import obtain_auth_token

from .views import login_user
# app_name = 'accounts'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_user, name='login'),
    path('test/', example_view, name='test'),
]