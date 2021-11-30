from django.db import models
from django.urls import reverse

# Create your models here.
class Tool(models.Model):
  name = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tools_detail', kwargs={'tool_id': self.id})