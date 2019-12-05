from django.urls import path
from apps.blog import views as post_views

app_name = 'blog'

urlpatterns = [
    path('',post_views.post_lists,name='post-lists'),
    path('post/@<str:post_author_username>/<str:post_slug>/',post_views.post_details,name='post_details'),    
]
