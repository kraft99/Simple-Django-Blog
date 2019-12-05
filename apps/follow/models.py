from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Follow(models.Model):
	"""  Model - Follow Model  """
	to_user 	= models.ForeignKey(settings.AUTH_USER_MODEL,\
	on_delete=models.CASCADE,related_name='following')# user to follow(following)
	from_user 	= models.ForeignKey(settings.AUTH_USER_MODEL,\
	on_delete=models.CASCADE,related_name='followers')# request user(followers)

	created 	= models.DateTimeField(auto_now_add=True)


	class Meta:
		unique_together = (('to_user','from_user'),)
		verbose_name 	= 'Follow'
		verbose_name_plural = 'Follows'


	def __str__(self):
		return "{0} is following {1}".format(self.from_user.username,self.to_user.username)


	def save(self,*args,**kwargs):
		# user can't follow self.
		not_allowed = self.to_user == self.from_user
		if not_allowed:
			raise PermissionDenied
		return super(Follow,self).save(*args,**kwargs)

	@classmethod
	def create_follow(cls,request_user,user_to_follow):
		"""
		check 
		1: is request_user is already following user_to_follow
		2: request_user cannot follow self
		"""
		if request_user == user_to_follow:
			raise PermissionDenied
		try:
			cls.objects.get(to_user =user_to_follow ,from_user = request_user)
		except cls.DoesNotExist:
			cls.objects.create(to_user =user_to_follow ,from_user = request_user)


	@classmethod
	def user_followers(cls,request_user):
		users_list = []
		if request_user and hasattr(request_user,'id'):
			try:
				user = User.objects.get(username__iexact = request_user.username)
				qryset = Follow.objects.filter(to_user = user)
				if qryset.exists():
					for follow_obj in qryset:
						users_list.append(follow_obj.from_user)
					return users_list
				return []
			except:
				pass
		raise Http404


	@property
	def count_followers(self):
		if Follow.user_followers(self.from_user):
			return len(Follow.user_followers(self.from_user))
		return 0



	@classmethod
	def user_following(cls,request_user):
		users_list = []
		if request_user:
			try:
				user = User.objects.get(username__iexact = request_user.username)
				qryset = cls.objects.filter(from_user = user)
				if qryset.count() > 0:
					for follow_obj in qryset:
						users_list.append(follow_obj.to_user)
					return users_list
				return []
			except:
				pass
		raise Http404



	def is_following(cls,request_user,user_to_follow):
		"""
		A is following B

		Logic:
		B followers must have A in it
		"""
		request_user_obj = User.objects.filter(id = request_user.id)
		if request_user and user_to_follow:
			user = User.objects.filter(username__iexact = user_to_follow.username)
			if not user is None:
				try:
					followers = cls.user_followers(user_to_follow)
					if request_user_obj in followers:
						return True
					return False
				except:
					pass
			else:
				pass
		




