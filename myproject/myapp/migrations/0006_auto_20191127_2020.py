# Generated by Django 2.2.7 on 2019-11-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20191125_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='myimage',
            field=models.FileField(default='hello', upload_to='post'),
        ),
    ]
