# Generated by Django 3.0.3 on 2020-12-15 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20201215_2327'),
        ('sales', '0008_auto_20201215_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='items.Item'),
        ),
    ]
