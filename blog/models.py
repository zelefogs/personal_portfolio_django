from django.db import models


class Blog(models.Model):
	title = models.TextField(max_length=150, name='title')
	date = models.DateField()
	description = models.CharField(max_length=250)
