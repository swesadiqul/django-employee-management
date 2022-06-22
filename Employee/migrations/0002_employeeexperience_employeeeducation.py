# Generated by Django 4.0.5 on 2022-06-20 03:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company1name', models.CharField(max_length=100, null=True)),
                ('company1desig', models.CharField(max_length=100, null=True)),
                ('company1salary', models.CharField(max_length=100, null=True)),
                ('company1duration', models.CharField(max_length=100, null=True)),
                ('company2name', models.CharField(max_length=100, null=True)),
                ('company2desig', models.CharField(max_length=100, null=True)),
                ('company2salary', models.CharField(max_length=100, null=True)),
                ('company2duration', models.CharField(max_length=100, null=True)),
                ('company3name', models.CharField(max_length=100, null=True)),
                ('company3desig', models.CharField(max_length=100, null=True)),
                ('company3salary', models.CharField(max_length=100, null=True)),
                ('company3duration', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolclgpg', models.CharField(max_length=100, null=True)),
                ('yearofpassingpg', models.CharField(max_length=20, null=True)),
                ('percentagepg', models.CharField(max_length=30, null=True)),
                ('coursegra', models.CharField(max_length=100, null=True)),
                ('schoolclggra', models.CharField(max_length=100, null=True)),
                ('yearofpassinggra', models.CharField(max_length=20, null=True)),
                ('percentagegra', models.CharField(max_length=30, null=True)),
                ('coursepg', models.CharField(max_length=100, null=True)),
                ('schoolclgssc', models.CharField(max_length=100, null=True)),
                ('yearofpassingssc', models.CharField(max_length=20, null=True)),
                ('percentagessc', models.CharField(max_length=30, null=True)),
                ('coursehsc', models.CharField(max_length=100, null=True)),
                ('schoolclghsc', models.CharField(max_length=100, null=True)),
                ('yearofpassinghsc', models.CharField(max_length=20, null=True)),
                ('percentagehsc', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]