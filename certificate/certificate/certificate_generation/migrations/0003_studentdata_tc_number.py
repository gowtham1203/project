# Generated by Django 4.2.2 on 2023-10-22 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_generation', '0002_alter_studentdata_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='tc_number',
            field=models.CharField(default=2, max_length=3),
            preserve_default=False,
        ),
    ]
