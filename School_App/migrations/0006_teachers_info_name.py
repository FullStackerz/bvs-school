# Generated by Django 5.0 on 2023-12-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School_App', '0005_teachers_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers_info',
            name='Name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
