# Generated by Django 4.0.3 on 2022-04-06 05:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.CharField(choices=[('open', 'Открытое'), ('closed', 'Закрытое')], default='open', max_length=20),
        ),
    ]
