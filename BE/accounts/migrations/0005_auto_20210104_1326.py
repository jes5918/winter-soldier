# Generated by Django 3.1.4 on 2021-01-04 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_group_todo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='todo',
        ),
        migrations.AddField(
            model_name='group',
            name='host',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]