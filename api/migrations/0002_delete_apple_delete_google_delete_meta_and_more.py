# Generated by Django 4.1.9 on 2023-06-07 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Apple',
        ),
        migrations.DeleteModel(
            name='Google',
        ),
        migrations.DeleteModel(
            name='Meta',
        ),
        migrations.DeleteModel(
            name='Microsoft',
        ),
    ]