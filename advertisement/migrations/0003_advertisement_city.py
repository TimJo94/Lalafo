# Generated by Django 4.0.3 on 2022-04-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_advertisement_created_at_alter_advertisement_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]