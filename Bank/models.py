from django.db import models
#from django.utils.timezone.now() import timezone.now
class details1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    bal=models.IntegerField(max_length=100);
class transcations(models.Model):
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    amt=models.IntegerField(max_length=100)
    dt=models.DateTimeField(auto_now=True)