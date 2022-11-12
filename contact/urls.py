from django.urls import path
from home.views import contact  
from .views import *

urlpatterns = [
    path('contact/', contact, name='contact'),
]