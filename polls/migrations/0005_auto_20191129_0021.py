# Generated by Django 2.2.5 on 2019-11-28 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_patient_patient_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Patient_Day',
            new_name='Medicine_morning',
        ),
    ]
