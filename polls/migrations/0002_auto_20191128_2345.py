# Generated by Django 2.2.5 on 2019-11-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Medicine_Morning',
        ),
        migrations.AddField(
            model_name='patient',
            name='Days',
            field=models.TextField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]