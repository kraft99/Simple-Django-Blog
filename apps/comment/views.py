from django.http import Http404
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse,HttpResponseRedirect
from apps.comment.decorators import user_is_comment_owner
from apps.activity.utils import create_action

from apps.comment.forms import CommentForm

from apps.comment.models import Comment



def comment_threads(request,comment_id):

	comment = None
	if not comment_id is None:
		try:
			comment = Comment.objects.get(id = int(comment_id))
			content_object = comment.content_object
			content_id = comment.content_object.id
		except:
			pass

	initial_setup = {
		"content_type":content_object.get_instance_content_type,
		"object_id": comment.object_id
	}
	# print(comment.is_parent)
	post = comment.content_object

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

		comment_obj 	= Comment(
					  user = request.user,
					  content  = content,
					  content_type = content_type,
					  object_id = obj_id,
					  parent = parent_obj,
					)
		comment_obj.save()
		create_action(request.user,'replied',comment_obj)
		return redirect('comment:comment-threads', comment_id = comment_id)# redirect to parent comment

	context = {}
	context['comment'] = comment
	context['post'] = post
	context['form'] = form
	template = 'comment/comment_threads.html'
	return render(request,template,context)



@user_is_comment_owner
def delete_comment(request,comment_id = None):
	if not comment_id is None:
		try:
			comment = Comment.objects.get(id = comment_id)
			if not comment.is_parent:
				redirect_url = comment.parent.get_absolute_url()
			else:
				redirect_url = comment.get_absolute_url()
		except:
			raise Http404()
		comment.delete()
	return redirect(redirect_url)
