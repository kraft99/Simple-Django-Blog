# Generated by Django 2.1.10 on 2019-10-18 18:18

import apps.common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191014_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bkgrd_pic',
            field=models.ImageField(default='', null=True, upload_to=apps.common.utils.upload_pic_location, verbose_name='pic'),
        ),
    ]
