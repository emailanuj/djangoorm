# Generated by Django 3.0.1 on 2019-12-28 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0005_staff_salry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='salry',
            new_name='salary',
        ),
    ]
