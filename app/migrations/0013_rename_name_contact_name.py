# Generated by Django 4.0.6 on 2022-08-25 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='Name',
        ),
    ]
