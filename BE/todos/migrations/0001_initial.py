# Generated by Django 3.1.4 on 2021-01-03 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('schedule_year', models.CharField(max_length=4)),
                ('schedule_month', models.CharField(max_length=2)),
                ('schedule_date', models.CharField(max_length=2)),
                ('schedule_hour', models.CharField(max_length=2)),
                ('schedule_min', models.CharField(max_length=2)),
                ('alarm_year', models.CharField(max_length=4)),
                ('alarm_month', models.CharField(max_length=2)),
                ('alarm_date', models.CharField(max_length=2)),
                ('alarm_hour', models.CharField(max_length=2)),
                ('alarm_min', models.CharField(max_length=2)),
                ('completed', models.CharField(default='no', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_todo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]