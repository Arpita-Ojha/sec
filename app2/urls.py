from django.urls import path
from app2.views import*
app_name='something2'

urlpatterns=[
    path('lucky/',lucky,name='lucky'),
    path('arpita/',arpita,name='arpita'),
]