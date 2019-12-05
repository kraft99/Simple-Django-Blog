from .managers import PostManager
from apps.common.slug_generator import unique_slug_generator
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils.text import Truncator
from django.utils import timezone
from django.contrib.auth import get_user_model


from apps.common import utils
from apps.common import functions
from apps.comment.models import Comment
from django.db import models




User = get_user_model()


DRAFT = 'draft'
PUBLISHED = 'published'

STATUS_CHOICES = (
	(DRAFT,'Draft'),
	(PUBLISHED,'Published'),
)




class Post(models.Model):
	"""
	Model - Post
	
	"""
	id  		= models.UUIDField(primary_key=True, default= utils.get_id_token, editable=False)
	title   	= models.CharField(max_length=125,verbose_name=_('title'))
	slug 		= models.SlugField(max_length=150,unique=True,null=True, blank=True)
	author  	= models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
	content 	= models.TextField(max_length=250)
	publish 	= models.DateTimeField(default = timezone.now)
	status  	= models.CharField(max_length=10,choices = STATUS_CHOICES,default=DRAFT)
	bkgrd_pic 	= models.ImageField(upload_to= utils.upload_pic_location,blank=False,null=True,default="",verbose_name='pic')
	views       = models.PositiveIntegerField(default=0,blank=True,null=True)
	readtime    = models.TimeField(blank=True,null=True)
	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)


	objects 	= PostManager() #registering Manager !

	class Meta:
		ordering = ('-publish',)
		verbose_name = _('post')
		verbose_name_plural = _('post')


	def __str__(self):
		truncate_content = Truncator(self.content)
		return truncate_content.chars(15) 


	def delete(self, *args, **kwargs):
		if self.bkgrd_pic:
			self.bkgrd_pic.delete(save = False)
		super().delete(*args,**kwargs)


	def get_absolute_url(self):
		return reverse('blog:post_details',
			args=[str(self.author.username),
			str(self.slug)])


	def get_delete_url(self):
		pass


	def get_edit_url(self):
		pass


	def post_published_ago(self):
		"""
		@purpose : a human readable time.
		Example : 2 minutes ago,1 hour ago,1 day,35 minutes ago ...
		"""
		return functions.human_readable_time(self.publish)
	time_ago = property(post_published_ago)



	@property
	def post_read_time(self):
    		# work on readtime - Bug !
		if self.content and len(self.content) > 0:
			return utils.get_words_read_time(self.content)
		return


	@property
	def post_comments(self):
		qry = Comment.objects.filter_by_model_instance(self)
		return qry



	@property
	def get_instance_content_type(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return content_type



	@classmethod
	def authors_blog_post_count(cls,post_obj):
		"""
		@purpose : total count of authors posts in the database.
		"""
		if post_obj:
			if post_obj.author:
				return post_obj.author.blog_posts.all().count()
			return 0



@receiver(pre_save,sender=Post)
def pre_save_post_receiver(sender,instance,*args,**kwargs):

	if instance.content:
		instance.readtime = str(utils.get_words_read_time(instance.content))

	#generate slug here
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)






