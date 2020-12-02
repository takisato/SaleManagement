# Generated by Django 3.0.3 on 2020-12-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_update_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
