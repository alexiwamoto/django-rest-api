from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Produto(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    thumb = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)

class Foto(models.Model):
    
    path = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    pub_date = models.DateField()
    produto = models.ForeignKey(Produto, related_name='fotos', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.path

    class Meta:
        # unique_together = ('produto', 'path')
        ordering = ['path']
    
    def __unicode__(self):
        return '%s: %s' % (self.name, self.path)
        
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



# class Order(Model):
#      order_name = CharField(max_length=10)

# class OrderDetails(Model):
#      order_detail_name = CharField(max_length=10)
#      order = ForeignKey('Order')
# I want to get/insert/update/delete OrderDetails with order object itself. If I post this json, it should insert/update both objects.

# {
#     "id": 10,
#     "order_name": "Some title",
#     "orderDetails": [{
#          "id": 15,
#          "order_detail_name": "Best Detail"
#      }]
# }