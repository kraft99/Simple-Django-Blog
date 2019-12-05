from django.urls import path
from apps.like import views as like_views

app_name = 'like'

urlpatterns = [
    path('post-like/',like_views.post_like,name='post-like'),
]
