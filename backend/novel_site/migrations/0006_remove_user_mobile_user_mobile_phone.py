# Generated by Django 4.1.1 on 2022-09-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel_site', '0005_user_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='手机号'),
        ),
    ]