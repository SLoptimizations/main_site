# Generated by Django 3.0.3 on 2020-05-14 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events_health', '0009_auto_20200514_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events_health.Event'),
        ),
    ]
