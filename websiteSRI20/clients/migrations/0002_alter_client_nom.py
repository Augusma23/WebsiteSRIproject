# Generated by Django 3.2 on 2021-04-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
