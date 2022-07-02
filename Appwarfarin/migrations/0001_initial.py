# Generated by Django 4.0.5 on 2022-07-02 12:46

import Appwarfarin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('password', models.CharField(default=Appwarfarin.models.Doctor.doctor, max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='INR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INR_name', models.CharField(max_length=100)),
                ('INR_Range_min', models.IntegerField()),
                ('INR_Range_max', models.IntegerField()),
                ('INR_Range_desc', models.CharField(max_length=100)),
                ('INR_Rtc_period', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('password', models.CharField(default=Appwarfarin.models.Nurse.nurse, max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Patient_name', models.CharField(max_length=100)),
                ('Patient_age', models.IntegerField()),
                ('Patient_Residence', models.CharField(max_length=100)),
                ('Patient_phone', models.IntegerField()),
                ('Patient_email', models.EmailField(max_length=100)),
                ('Patient_Bp', models.IntegerField()),
                ('Patient_weight', models.IntegerField()),
                ('Patient_height', models.IntegerField()),
                ('Patient_temperature', models.IntegerField()),
                ('Patient_Inr', models.IntegerField()),
                ('Patient_Diagnosis', models.CharField(max_length=100)),
            ],
        ),
    ]
