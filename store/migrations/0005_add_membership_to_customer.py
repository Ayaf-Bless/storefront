# Generated by Django 3.2.5 on 2021-07-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_add_zip_to_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='membership',
            field=models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'Gold')], default='B', max_length=1),
        ),
    ]
