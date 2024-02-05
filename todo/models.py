from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    dedline = models.DateTimeField(blank=True, null=True)
    implementation = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
