# Generated by Django 2.1.7 on 2019-03-29 21:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190325_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cd7715ba-4779-4b36-9b19-1f2973553e72'), editable=False, primary_key=True, serialize=False),
        ),
    ]