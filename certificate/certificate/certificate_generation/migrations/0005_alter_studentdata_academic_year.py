# Generated by Django 4.2.2 on 2023-10-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_generation', '0004_alter_studentdata_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='academic_year',
            field=models.IntegerField(max_length=7),
        ),
    ]
