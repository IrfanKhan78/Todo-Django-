from django.db import models

# Create your models here.

class Todo(models.Model):
	content = models.TextField(max_length=500)

	def __str__(self):
		return 'Task #{}: {}'.format(self.id, self.content)
