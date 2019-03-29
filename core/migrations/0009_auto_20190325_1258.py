# Generated by Django 2.1.7 on 2019-03-25 12:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190325_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ('-time',)},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('030717ad-182d-475f-a701-4eb5f005bd9f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.DateTimeField(auto_created=True),
        ),
    ]