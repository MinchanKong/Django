from django.db import models
from django.utils import timezone

# Create your models here.
class Status(models.Model):
	time = models.DateTimeField(
		default=timezone.now)
	user = models.CharField(max_length=50)
	result = models.CharField(max_length=20)
