from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=False)

    def __str__(self):
        return self.title
