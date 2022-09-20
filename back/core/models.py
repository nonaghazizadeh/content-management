from django.db import models
from django.contrib.auth.models import User


def content_directory_path(instance, filename):
    return f'{instance.title}_{instance.file_format}_{filename}'


def attach_directory_path(instance, filename):
    return f'attach_{instance.title}_{instance.file_format}_{filename}'


class Content(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=20)
    file_format = models.CharField(
        max_length=1,
        choices=[
            ('V', 'Video'),
            ('A', 'Audio'),
            ('D', 'Document'),
            ('I', 'Image')
        ]
    )
    file = models.FileField(upload_to=content_directory_path)
    attach_file = models.FileField(upload_to=attach_directory_path, null=True)
    extra = models.JSONField()

    class Meta:
        unique_together = (('title', 'file_format'),)
