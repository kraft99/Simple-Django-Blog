from apps.common import functions
from django.conf import settings
from apps.comment import managers
from django.urls import reverse
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.db import models




class Comment(models.Model):

	user			= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="comments")
	content			= models.TextField(max_length=350,null=True,blank=True)

	content_type 	= models.ForeignKey(ContentType, on_delete=models.CASCADE) #Post Model
	# use CharField for uuid in generic - to resolve error with (SqlLite) Big Integer
	object_id 		= models.CharField(max_length = 120,blank=True,null=True) #post instance id
	content_object 	= GenericForeignKey('content_type', 'object_id') #combine Post Model & post instance id

	parent 			= models.ForeignKey("self",null=True,blank=True,on_delete=models.SET_NULL) #reply == comment

	created			= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)

	objects 		= managers.CommentManager()


	class Meta:
		ordering = ('-created',)


	def __str__(self):
		return "{0}".format(self.content)


	def get_absolute_url(self):
		return reverse('comment:comment-threads',args=[int(self.id)])




	def get_delete_url(self):
		return reverse('comment:comment-delete',args=[int(self.id)])



	@property
	def humantime(self):
		return functions.human_readable_time(self.created)


	#reply
	def children(self):
		cls = Comment
		return cls.objects.filter(parent = self)
	reply = property(children)


	# is_parent?
	@property
	def is_parent(self):
		if not self.parent is None:
			return False
		return True


	def find_parent_of_child(cls,reply_obj):
		pass
