# Generated by Django 2.2.6 on 2019-10-07 15:46

import apps.common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191007_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bkgrd_pic',
            field=models.ImageField(default='', null=True, upload_to=apps.common.utils.upload_pic_location),
        ),
    ]
