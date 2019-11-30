# Generated by Django 2.2.7 on 2019-11-17 05:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=30)),
                ('description', models.TextField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
