# Generated by Django 3.0.5 on 2021-01-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libmanage', '0005_auto_20210104_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bid',
        ),
        migrations.AlterField(
            model_name='borrower',
            name='fine',
            field=models.IntegerField(default=0),
        ),
    ]
