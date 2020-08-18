# Generated by Django 2.2.5 on 2019-11-28 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_information',
            name='Medicine_morning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient_information',
            name='Medicine_night',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient_information',
            name='Medicine_noon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient_information',
            name='Patient_Rx',
            field=models.CharField(blank=True, choices=[('Renava', 'Renava'), ('napa', 'napa'), ('opton', 'opton'), ('ctz', 'ctz')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='patient_information',
            name='Per_day',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_information',
            name='Provided_Medicine',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_information',
            name='Total_medicine',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]