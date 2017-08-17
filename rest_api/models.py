from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Produto(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Foto(models.Model):
    path = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    pub_date = models.DateField()
    produto = models.ForeignKey(Produto, related_name='fotos', on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.path

    class Meta:
        unique_together = ('produto', 'path')
        ordering = ['path']
    
    def __unicode__(self):
        return '%s: %s' % (self.name, self.path)

# class Album(models.Model):
#     album_name = models.CharField(max_length=100)
#     artist = models.CharField(max_length=100)

# class Track(models.Model):
#     album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
#     order = models.IntegerField()
#     title = models.CharField(max_length=100)
#     duration = models.IntegerField()

#     class Meta:
#         unique_together = ('album', 'order')
#         ordering = ['order']

#     def __unicode__(self):
#         return '%d: %s' % (self.order, self.title)

# class Bucketlist(models.Model):
#     """This class represents the bucketlist model."""
#     name = models.CharField(max_length=255, blank=False, unique=True)
#     owner = models.ForeignKey(
#         'auth.User',
#         related_name='bucketlists',
#         on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         """Return a human readable representation of the model instance."""
#         return "{}".format(self.name)

# This receiver handles token creation when a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



