# Generated by Django 2.1.10 on 2019-10-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20191015_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(blank=True, default='', max_length=6, null=True, unique=True),
        ),
    ]