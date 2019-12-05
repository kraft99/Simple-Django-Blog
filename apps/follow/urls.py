from django.urls import path
from apps.follow import views as follow_views

app_name = 'follow'

urlpatterns = [
    path('',follow_views.follow,name='follow-user'),
]
