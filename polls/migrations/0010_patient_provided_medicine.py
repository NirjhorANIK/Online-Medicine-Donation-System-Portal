# Generated by Django 2.2.5 on 2019-11-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_patient_total_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Provided_Medicine',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
