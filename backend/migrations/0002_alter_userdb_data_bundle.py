# Generated by Django 5.0 on 2024-01-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='Data_Bundle',
            field=models.CharField(blank=True, choices=[('3_GHS__340MB', '3 Ghs  340Mb'), ('5_GHS__740MB', '5 Ghs  740Mb'), ('10_GHS__1GB', '10 Ghs  1Gb')], default='', max_length=15),
        ),
    ]
