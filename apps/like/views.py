from django.urls import reverse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.decorators.http import require_http_methods
from apps.common.decorators import ajax_required
from django.contrib.auth import get_user_model
from apps.activity.utils import create_action
from apps.blog.models import Post
from .models import Like




@ajax_required
@require_http_methods(["POST"])
def post_like(request):
	post_id = request.POST.get('post-id')
	post = get_object_or_404(Post,id = str(post_id.strip()))

	User = get_user_model()
	username = request.POST.get('username')
	request_user = get_object_or_404(User,username__iexact=username.strip())
	
	is_liked = True
	like_obj,created = Like.objects.get_or_create(post = post,user = request_user)
	if not created:
		# already exist - delete it !
		like_obj = Like.objects.filter(post = post,user = request_user)
		like_obj.delete()
		is_liked = False
	else:
    	create_action(request_user,'Liked',post)
		count = post.likes.count()
		response = {'is_liked':is_liked,'count':count}
	return JsonResponse(response)

