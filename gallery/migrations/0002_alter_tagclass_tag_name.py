# Generated by Django 3.2.5 on 2021-07-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagclass',
            name='tag_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
