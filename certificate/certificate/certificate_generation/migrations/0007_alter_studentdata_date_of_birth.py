# Generated by Django 4.2.6 on 2023-10-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_generation', '0006_alter_studentdata_academic_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='date_of_birth',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
