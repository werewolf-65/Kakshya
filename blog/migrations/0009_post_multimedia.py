# Generated by Django 2.1.5 on 2019-02-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='multimedia',
            field=models.FileField(blank=True, null=True, upload_to='gallery/'),
        ),
    ]
