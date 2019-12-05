from django.db import models
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import Http404
from apps.blog.models import Post
from django.contrib.auth.models import User



class Like(models.Model):
	"""
	Model 	- Like

	(Fields)
	post 	- int (foreignkey)
	user  	- user model (foreignkey)

	created - datetime object
	updated - datetime object

	
	"""
	post 	= models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
	user 	= models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_liked')

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		unique_together = (("post", "user"),)
		verbose_name = 'Like'
		verbose_name_plural = 'Likes'



	def __str__(self):
		return "{0} liked by {1}".format(self.post.title,self.user.username)



	@classmethod
	def user_has_liked_post(cls,post_id,user_obj):
		# return False if user has not liked post else True
		if user_obj.is_authenticated and user_obj.is_active:
			try:
				post_obj = Post.objects.get(id = str(post_id))
				qry = post_obj.likes.filter(user = user_obj).exists()
				if qry:
					return True
				return False
			except Post.DoesNotExist:
				# assume post object does not exists.
				raise Http404()
		else:
			pass


	@classmethod
	def post_likes_count(cls,post_id):
		# return a post likes count,given a post object. 
		if post_id and not post_id is None:
			post_obj = get_object_or_404(Post,id = str(post_id))
			return post_obj.likes.count()
		else:
			pass


