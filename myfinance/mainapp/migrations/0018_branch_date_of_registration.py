# Generated by Django 4.2.4 on 2023-09-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_delete_group_info_my_group_date_of_registration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='date_of_registration',
            field=models.DateField(blank=True, null=True),
        ),
    ]
