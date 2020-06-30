from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings

ISSUE_CHOICE = (
	('abandoned', 'Abandoned'),
	('resolved', 'Resolved'),
)

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default= timezone.now())
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	issue = models.CharField(max_length=25,choices= ISSUE_CHOICE, default='abandoned')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Agent(models.Model):
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	assigned_time = models.DateTimeField(default= timezone.now())
	start_date = models.DateTimeField(null=True)
	date_commit = models.DateTimeField(null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_user_set')
	assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='assigned_to_user_set')

	def __str__(self):
		return str(self.assigned_to)

	def get_absolute_url(self):
		return reverse('agent-detail')
