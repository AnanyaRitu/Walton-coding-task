# Generated by Django 4.2.3 on 2023-07-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
