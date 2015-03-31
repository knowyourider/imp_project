from django.db import models

class Artifact(models.Model):
	STATUS_NUMS = (
		(1,'1 - Entered'),
		(2,'2 - TBD'),
		(3,'3 - Work in progress'),
		(4,'4 - Published'),
	)
	short_name = models.CharField(max_length=32, unique=True)
	title = models.CharField(max_length=128)
	description = models.TextField('Description - Label', blank=True, null=True)
	notes = models.TextField('Production Notes', blank=True, null=True)
	status_num = models.IntegerField(default=0, choices=STATUS_NUMS)
	def __str__(self):
		return self.title
