# Generated by Django 2.2.1 on 2019-08-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20190819_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reserved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]