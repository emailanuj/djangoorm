# Generated by Django 3.0.1 on 2019-12-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0006_auto_20191228_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cutomer_type',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]