# Generated by Django 4.1.7 on 2023-03-21 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_alter_orderitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='dae',
            new_name='date',
        ),
    ]