# Generated by Django 2.2.1 on 2019-08-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0003_auto_20190630_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='poster_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
