# Generated by Django 4.0.3 on 2022-04-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_orderplaced_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FE', 'Equipment'), ('FA', 'Accessories'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear')], max_length=2),
        ),
    ]
