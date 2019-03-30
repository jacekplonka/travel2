# Generated by Django 2.1.7 on 2019-03-30 12:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190329_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('474208e2-9c11-44c2-a503-d2c343442ce7'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo10',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo2',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo3',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo4',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo5',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo6',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo7',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo8',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='photo9',
            field=models.ImageField(blank=True, default='null', null=True, upload_to='trips'),
        ),
    ]
