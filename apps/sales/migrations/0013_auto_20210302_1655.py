# Generated by Django 3.0.3 on 2021-03-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_auto_20210302_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='profit',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
