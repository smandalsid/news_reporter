# Generated by Django 4.1.9 on 2023-06-07 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_apple__id_alter_google__id_alter_meta__id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apple',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='google',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meta',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='microsoft',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
