from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255, default='Без заголовка')
    file = models.FileField(upload_to='upload/', max_length=255, null=True, blank=True)
    authors = models.JSONField(default=list)
    year = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    file_path = models.CharField()

    def __str__(self):
        return self.title
