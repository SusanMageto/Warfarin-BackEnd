# Generated by Django 3.2 on 2022-07-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20220707_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paitentprofile',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='paitentprofile',
            old_name='last_name',
            new_name='residence',
        ),
        migrations.RemoveField(
            model_name='paitentprofile',
            name='case',
        ),
        migrations.RemoveField(
            model_name='paitentprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='paitentprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='paitentprofile',
            name='bp',
            field=models.PositiveIntegerField(default=21),
        ),
        migrations.AddField(
            model_name='paitentprofile',
            name='diagnosis',
            field=models.CharField(default='Continue with the previous dose of ...  RTC 2 to 4 Weeks', max_length=50),
        ),
        migrations.AddField(
            model_name='paitentprofile',
            name='email',
            field=models.EmailField(default='patient@gmail.com', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='paitentprofile',
            name='height',
            field=models.CharField(default='1.75m', max_length=50),
        ),
        migrations.AddField(
            model_name='paitentprofile',
            name='inr_range',
            field=models.PositiveIntegerField(default=2.4),
        ),
        migrations.AddField(
            model_name='paitentprofile',
            name='temparature',
            field=models.PositiveIntegerField(default=37),
        ),
        migrations.AddField(
            model_name='paitentprofile',
            name='weight',
            field=models.CharField(default='60 kgs', max_length=50),
        ),
    ]