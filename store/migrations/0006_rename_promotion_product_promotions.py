# Generated by Django 3.2.5 on 2021-07-27 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_add_membership_to_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='promotion',
            new_name='promotions',
        ),
    ]