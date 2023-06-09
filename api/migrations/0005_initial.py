# Generated by Django 4.1.9 on 2023-06-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0004_delete_apple_delete_google_delete_meta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(default='Apple', editable=False, max_length=10)),
                ('batch', models.CharField(max_length=500)),
                ('title', models.TextField(max_length=1000)),
                ('link', models.TextField(max_length=2000)),
                ('ago', models.DateField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(default='Google', editable=False, max_length=10)),
                ('batch', models.CharField(max_length=500)),
                ('title', models.TextField(max_length=1000)),
                ('link', models.TextField(max_length=2000)),
                ('ago', models.DateField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(default='Meta', editable=False, max_length=10)),
                ('batch', models.CharField(max_length=500)),
                ('title', models.TextField(max_length=1000)),
                ('link', models.TextField(max_length=2000)),
                ('ago', models.DateField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Microsoft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(default='Microsoft', editable=False, max_length=10)),
                ('batch', models.CharField(max_length=500)),
                ('title', models.TextField(max_length=1000)),
                ('link', models.TextField(max_length=2000)),
                ('ago', models.DateField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
