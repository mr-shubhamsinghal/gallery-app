from django.db import models


class TagClass(models.Model):
	tag_name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.tag_name


class ImageClass(models.Model):
	image = models.FileField(upload_to='images/')
	tags = models.ManyToManyField(TagClass)

	class Meta:
		ordering = ['-id']
