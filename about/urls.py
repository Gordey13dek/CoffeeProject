from django.urls import path
from home.views import about  
from .views import *

urlpatterns = [
    path('about/', about, name='about'),
]