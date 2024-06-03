from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
  msg = models.TextField()
  sender = models.ForeignKey(User , on_delete=models.CASCADE)
  sent_at = models.DateTimeField(auto_now_add=True)

class ContactMsg(models.Model):
  name = models.CharField(max_length=200)
  contact = models.CharField(max_length=20)
  email = models.EmailField()
  msg = models.TextField()

  def __str__(self):
    return self.name