# Generated by Django 3.0.3 on 2020-12-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20201209_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='num',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='profit',
            field=models.PositiveIntegerField(),
        ),
    ]
