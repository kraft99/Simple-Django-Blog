# Generated by Django 2.2.6 on 2019-10-15 01:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20191015_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, default='', max_length=7, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together={('owner', 'code')},
        ),
    ]
