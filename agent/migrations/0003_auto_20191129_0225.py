# Generated by Django 2.2.5 on 2019-11-28 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_auto_20191129_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_information',
            name='Medicine_morning',
        ),
        migrations.RemoveField(
            model_name='patient_information',
            name='Medicine_night',
        ),
        migrations.RemoveField(
            model_name='patient_information',
            name='Medicine_noon',
        ),
        migrations.RemoveField(
            model_name='patient_information',
            name='Patient_Rx',
        ),
        migrations.RemoveField(
            model_name='patient_information',
            name='Per_day',
        ),
        migrations.RemoveField(
            model_name='patient_information',
            name='Provided_Medicine',
        ),
        migrations.RemoveField(
            model_name='patient_information',
            name='Total_medicine',
        ),
    ]
