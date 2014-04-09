from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

UserModel = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class Watch(models.Model):
    subscriber     = models.ForeignKey(UserModel, verbose_name="Subscriber")
    content_type   = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey()
    object_id      = models.IntegerField('object ID')
    created        = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0}".format(self.content_object)

    def get_absolute_url(self):
        """ 
        Use original content object's 
        get_absolute_url method.
        """
        return self.content_object.get_absolute_url()

    def get_last_modified(self):
        obj = self.content_object
        if obj.updated:
            return obj.updated
        if obj.modified:
            return obj.modified
