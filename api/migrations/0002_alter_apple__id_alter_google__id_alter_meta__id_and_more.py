# Generated by Django 4.1.9 on 2023-06-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apple',
            name='_id',
            field=models.IntegerField(auto_created=True, max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='google',
            name='_id',
            field=models.IntegerField(auto_created=True, max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meta',
            name='_id',
            field=models.IntegerField(auto_created=True, max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='microsoft',
            name='_id',
            field=models.IntegerField(auto_created=True, max_length=500, primary_key=True, serialize=False),
        ),
    ]
