from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.user_signup,name='signup'),
    
]