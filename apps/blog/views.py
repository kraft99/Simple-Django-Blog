from apps.common import functions

from django.urls import reverse
from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.http import (HttpResponseNotFound,HttpResponseServerError,
						HttpResponseForbidden,Http404)
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.template import loader,RequestContext
from apps.activity.utils import create_action


from apps.comment.forms import CommentForm
from apps.comment.models import Comment
from apps.like.models import Like

from .models import Post




# def http403_handler(request):
# 	t = loader.get_template('pages/403.html')
# 	return HttpResponseForbidden(t.render(RequestContext(request,{'request_path':request.path})))



# def http404_handler(request):
# 	t = loader.get_template('pages/404.html')
# 	return HttpResponseNotFound(t.render(RequestContext(request,{'request_path':request.path})))


# def http500_handler(request):
# 	t = loader.get_template('pages/500.html')
# 	return HttpResponseServerError(t.render(RequestContext(request,{'request_path':request.path})))



def post_lists(request):

	posts = Post.objects.all()
	paginator = Paginator(posts,3)
	page = request.GET.get('page')
	context = {}
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# deliver first page
		posts = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			# ajax request return empty page
			return HttpResponse('')
		#out of range page - deliver last page
		posts = paginator.page(paginator.num_pages)
	if request.is_ajax():
		template = 'partials/_list_ajax.html'
		context['posts'] = posts
		return render(request,template,context)

	context['posts'] = posts
	template = 'blog/lists.html'
	return render(request,template,context)





def post_details(request,post_author_username,post_slug):

	is_auth = functions.is_user_authenticated(request)# user js - to  toggle auth-social-modal 
	post = get_object_or_404(Post,
							author__username = post_author_username,
							slug = post_slug)

	# print(post.__class__)
	authors_post_count = Post.authors_blog_post_count(post)

	post_url = request.build_absolute_uri(post.get_absolute_url())
	facebook_share = "https://www.facebook.com/sharer/sharer.php?u={0}".format(post_url)
	google_plus_share   = "https://plus.google.com/share?url={0}".format(post_url)

	flag = Like.user_has_liked_post(post.id,request.user)
	post_likes_count = post.likes.count()

	context = dict()
	# comment form
	initial_setup = {
	"content_type":post.get_instance_content_type,
	"object_id": post.id
	}
	# print(post.get_instance_content_type)
	form = CommentForm(data = request.POST or None,initial = initial_setup)
	if form.is_valid():
		# print(request.POST)
		cd = form.cleaned_data
		ctype = cd.get('content_type')
		content_type = ContentType.objects.get(model = ctype)
		obj_id = cd.get('object_id')
		content = cd.get('content')
		parent_obj = None
		try:
			parent_id = int(request.POST.get('parent_id'))
		except:
			parent_id = None 

		if parent_id:
			parent_qry = Comment.objects.filter(id = parent_id)
			if parent_qry.exists() and parent_qry.count() == 1:
				parent_obj = parent_qry.first()

		comment 	= Comment(
					  user = request.user,
					  content  = content,
					  content_type = content_type,
					  object_id = obj_id,
					  parent = parent_obj,
					)
		comment.save()
		create_action(request.user,'commented',comment)
		return redirect(post.get_absolute_url())


	context['form'] = form

	comments = post.post_comments

	session_key = 'viewed_post_{}'.format(post.id)
	if not request.session.get(session_key,False):
		post.views += 1
		post.save()
		request.session[session_key] = True

	context['post'] = post
	context['author_posts_count'] = authors_post_count
	context['facebook_share'] = facebook_share
	context['google_plus_share'] = google_plus_share
	context['post_url'] = post_url
	context['is_likes'] = flag
	context['likes_count'] = post_likes_count
	context['is_auth'] = is_auth
	context['comments'] = comments
	
	template = 'blog/detail.html'
	return TemplateResponse(request,template,context)

