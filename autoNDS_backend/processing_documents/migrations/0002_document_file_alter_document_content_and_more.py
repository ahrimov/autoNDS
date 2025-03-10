# Generated by Django 4.2.19 on 2025-03-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing_documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='file_path',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(default='Без заголовка', max_length=255),
        ),
    ]
