# Generated by Django 3.0 on 2020-08-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]