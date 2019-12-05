from django.urls import path
from apps.comment import views as comment_views

app_name = 'comment'

urlpatterns = [
    path('comment-thread/<int:comment_id>/',comment_views.comment_threads,name='comment-threads'),
    path('comment-thread/delete/<int:comment_id>/',comment_views.delete_comment,name='comment-delete'),
]
