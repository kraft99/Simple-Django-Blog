# Generated by Django 2.2.6 on 2019-10-08 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
