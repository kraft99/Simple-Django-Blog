import logging
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

logger = logging.getLogger(__name__)

class TimeStampedModel(models.Model):
    """ TimeStampedModel Model"""
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created",)



class NewsLetter(TimeStampedModel):
    """  NewsLetter Model """
    email  = models.CharField(max_length = 150)
    ip     = models.GenericIPAddressField(null=True,blank=True)


    class Meta:
        verbose_name        = "NewsLetter"
        verbose_name_plural = "NewsLetter's"


    def __str__(self):
        return self.email
    


    def comfirmation_mail(self):
        raise NotImplementedError


    @classmethod
    def email_exists(cls,email):
        
        if email and isinstance(email,str):
            email = email.strip()
            try:
                cls.objects.get(email__iexact = email)
            except cls.DoesNotExist:
                # email doesn't exist in db
                return False
            # email already exist in db
            return True




    @classmethod
    def add_email_to_newsletter(cls,email,ip = None):
        
        if not cls.email_exists(email):
            # email doesn't exist in db --> create it !
            if not ip is None:
                cls.objects.create(email=email,ip = ip)
            else:
                cls.objects.create(email=email)
            return True
        # wasn't successful --> no change in db
        return False
    


    @classmethod
    def subscribe_to_newsletter(cls,email):
        
        if not cls.email_exists(email):
            return cls.add_email_to_newsletter(email)
        return False



    @classmethod
    def unsubscribe_to_newsletter(cls,email):
        
        if cls.email_exists(email):
            # email exists
            try:
                newsletter_obj = cls.objects.get(email__iexact=email)
            except cls.DoesNotExist:
                from django.http import Http404
                raise Http404
            newsletter_obj.delete()
            return True # successful -- change in db !
        return False # no email of such exists !
        
            
        

     
        
        
