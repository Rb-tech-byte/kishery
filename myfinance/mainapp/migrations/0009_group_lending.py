# Generated by Django 4.2.4 on 2023-09-01 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_lending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('returned_amount', models.FloatField(blank=True, default='0.0', null=True)),
                ('interest', models.FloatField(blank=True, default='0.0', null=True)),
                ('lending_date', models.DateField(blank=True, null=True)),
                ('date_of_return', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected'), ('cleared', 'cleared')], default='pending', max_length=50)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.branch')),
                ('members', models.ManyToManyField(to='mainapp.member')),
                ('referee', models.ManyToManyField(to='mainapp.individual_ref')),
            ],
        ),
    ]
