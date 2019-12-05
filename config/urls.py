from django.conf import settings
from django.conf.urls.static import static

from apps.blog import views as blog_views

from django.contrib import admin
from django.urls import path,include




# handler403 = blog_views.http403_handler #permission denied error
# handler404 = blog_views.http404_handler #page not found error
# handler500 = blog_views.http500_handler #server error


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.blog.urls',namespace='blog')),
    path('like/',include('apps.like.urls',namespace='like')),
    path('comments/',include('apps.comment.urls',namespace='comment')),
    path('follow/',include('apps.follow.urls',namespace='follow')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)