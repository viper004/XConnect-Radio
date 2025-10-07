from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('chat',views.chat,name='chat'),
]