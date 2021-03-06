# Generated by Django 3.1.7 on 2021-04-25 18:38

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marketer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=300)),
                ('password', models.IntegerField()),
                ('full_name', models.CharField(max_length=300)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
