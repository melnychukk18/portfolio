from django.db import models

class WorkType(models.Model):
	name = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now_add=True)

class WorkImage(models.Model):
	image = models.FileField(upload_to="work/images/")

class WorkItem(models.Model):
	type = models.ManyToManyField(WorkType)

	name = models.CharField(max_length=200)
	text = models.TextField(max_length=2000)

	client = models.CharField(max_length=200)
	role = models.CharField(max_length=500)
	included = models.CharField(max_length=500)
	url = models.CharField(max_length=300)

	image = models.ManyToManyField(WorkImage)

	thumbnail = models.FileField(upload_to="work/thumbnails/")
	pub_date = models.DateTimeField(auto_now_add=True)


