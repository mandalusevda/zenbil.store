# Generated by Django 3.1.7 on 2021-04-20 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('size', models.IntegerField()),
                ('price', models.IntegerField()),
                ('body', models.TextField()),
                ('cdate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
