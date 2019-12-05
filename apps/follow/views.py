from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.follow.models import Follow




def follow(request):
	followers = Follow.user_followers(request.user)
	following = Follow.user_following(request.user)
	# f = Follow.objects.last()
	# print(f.count_followers)
	print(followers)
	print(following)
	return HttpResponse("Follow Me")