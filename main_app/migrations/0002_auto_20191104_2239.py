# Generated by Django 2.2.6 on 2019-11-04 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='ocassion',
            new_name='occasion',
        ),
    ]