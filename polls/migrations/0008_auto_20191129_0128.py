# Generated by Django 2.2.5 on 2019-11-28 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_patient_total_medicine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Total_Medicine',
            new_name='Per_day',
        ),
    ]
