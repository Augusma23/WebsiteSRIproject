# Generated by Django 3.2 on 2021-04-17 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commandes', '0002_auto_20210417_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='clint',
            new_name='client',
        ),
    ]
