# Generated by Django 4.1.1 on 2022-09-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel_site', '0007_authors_novel_novels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='novel_page_count',
            field=models.IntegerField(default=0, verbose_name='小说当前章节数'),
        ),
    ]
