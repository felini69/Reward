from django.urls import path
from .views import *

app_name = 'extra'


urlpatterns = [
    path('terms/', terms_view, name='terms'),
]