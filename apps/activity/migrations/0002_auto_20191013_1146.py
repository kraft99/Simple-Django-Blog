# Generated by Django 2.2.6 on 2019-10-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='target_id',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]
