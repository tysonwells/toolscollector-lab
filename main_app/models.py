from django.db import models
from django.urls import reverse

# Create your models here.
class Tool(models.Model):
  name = models.CharField(max_length=100)
  manufacturer = models.CharField(max_length=100)
  modelNumber = models.CharField(blank=True, max_length=50)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tools_detail', kwargs={'tool_id': self.id})