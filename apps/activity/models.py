from django.db import models
from django.conf import settings

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Best place to use it is in a model class together with a notification (Real Time)


class Action(models.Model):
    """   Action Model  
    
    # exclude login user inn action filter.
    action_exc = Action.objects.exclude(user = request.user)
    for action_obj in action_exc:
        action_obj.user,action_obj.verb,action_target
      
    """
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='actions',on_delete=models.CASCADE)
    verb        = models.CharField(max_length = 12,blank=True,null=True)

    target_ct   = models.ForeignKey(ContentType,blank=True,null=True,related_name='target_obj',on_delete=models.CASCADE)
    target_id   = models.CharField(null=True,blank=True,max_length=125)
    target      = GenericForeignKey('target_ct','target_id')

    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)



