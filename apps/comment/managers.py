from django.contrib.contenttypes.models import ContentType
from django.db import models

class CommentManager(models.Manager):

	def all(self):
		qry = super(CommentManager,self).filter(parent = None)
		return qry

	def filter_by_model_instance(self,model_instance):
		content_type = ContentType.objects.\
		get_for_model(model_instance.__class__,for_concrete_model=True)
		object_id = model_instance.id
		
		qry = super(CommentManager,self).\
			filter(content_type=content_type,
			object_id = object_id).filter(parent = None)
		return qry