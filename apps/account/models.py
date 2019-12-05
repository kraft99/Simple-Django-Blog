
from apps.common import uploades #typo
from django.conf import settings
from django.db import models


AUTH_USER_MODEL = settings.AUTH_USER_MODEL


class TimeStampedModel(models.Model):

    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# TODO : use imageKit - blank & white,watermark,thumbnails etc

class Profile(TimeStampedModel):

    owner       = models.OneToOneField(AUTH_USER_MODEL,
                                     verbose_name="owner",
                                     related_name="profile",
                                     on_delete=models.CASCADE)

    pic         = models.ImageField(upload_to=uploades.upload_loc,
                                     blank=True,
                                     null=True,
                                     validators=[uploades.validate_uploaded_file_size_and_extension],
                                     default=uploades.get_default_avatar_url) #remove this, random avatar working now !
    
    code        = models.CharField(max_length=6,default='',unique=True,blank=True,null=True)

    bio         = models.TextField(max_length=500,blank=True,null=True,default="")


    class Meta:
        ordering = (("-created"),)
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        unique_together = (('owner','code'),)


    def __str__(self):
        return self.owner.username

    
    @property
    def pic_url(self):
        if self.pic:
            return self.pic.url
        return uploades.get_default_avatar_url()
    



