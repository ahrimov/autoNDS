from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255)
    authors = models.JSONField(default=list)
    year = models.IntegerField(null=True, blank=True)
    content = models.TextField()
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.title
