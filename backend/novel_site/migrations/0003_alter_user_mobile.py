# Generated by Django 4.1.1 on 2022-09-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel_site', '0002_alter_user_current_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, verbose_name='手机号'),
        ),
    ]
