# Generated by Django 4.0.5 on 2022-07-02 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appwarfarin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='nurse',
            old_name='name',
            new_name='username',
        ),
    ]
