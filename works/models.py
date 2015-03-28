from django.db import models

class WorkType(models.Model):
	name = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

class WorkImage(models.Model):
	image = models.FileField(upload_to="work/images/")
	image_alt = models.TextField(blank=True)

class WorkItem(models.Model):
	type = models.ManyToManyField(WorkType)

	name = models.CharField(max_length=200)
	text = models.TextField(max_length=2000, blank=True)
	thumb_text = models.TextField(max_length=300)

	client = models.CharField(max_length=200)
	role = models.CharField(max_length=500, blank=True)
	included = models.CharField(max_length=500, blank = True)
	url = models.CharField(max_length=300, blank=True)

	image = models.ManyToManyField(WorkImage, blank=True)

	thumbnail = models.FileField(upload_to="work/thumbnails/")
	pub_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name

	def get_next(self):
	    next = WorkItem.objects.filter(id__gt=self.id)
	    if next:
	      return next[0]
	    return False

	def get_prev(self):
		prev = WorkItem.objects.filter(id__lt=self.id).order_by('-id')
		if prev:
			return prev[0]
		return False


