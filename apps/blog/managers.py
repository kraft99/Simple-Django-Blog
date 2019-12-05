from django.db import models


class PostQuerySet(models.QuerySet):
	"""
	Custom QuerySet is required for chaining purpose	
	"""
	def published(self):
		return self.filter(status="published")



class PostManager(models.Manager):

	def get_queryset(self):
		return PostQuerySet(self.model,using=self._db) # important !

	def published(self):
		"""
		@use:
		Post.objects.published()
		Post.objects.filter(author = request.user).published().all()
		...

		"""
		return self.get_queryset().published()