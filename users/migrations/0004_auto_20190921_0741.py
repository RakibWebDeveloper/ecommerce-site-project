# Generated by Django 2.2.5 on 2019-09-21 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190921_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
