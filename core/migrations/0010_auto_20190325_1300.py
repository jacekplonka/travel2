# Generated by Django 2.1.7 on 2019-03-25 13:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190325_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('32471089-22cc-494d-8371-58bf2a938c4d'), editable=False, primary_key=True, serialize=False),
        ),
    ]