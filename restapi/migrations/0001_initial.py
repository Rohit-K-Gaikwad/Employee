# Generated by Django 4.2.7 on 2023-11-25 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseno', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualificationName', models.CharField(max_length=100)),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phoneNo', models.CharField(max_length=20)),
                ('addressDetails', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restapi.addressdetails')),
                ('projects', models.ManyToManyField(to='restapi.project')),
                ('qualifications', models.ManyToManyField(to='restapi.qualification')),
                ('workExperience', models.ManyToManyField(to='restapi.workexperience')),
            ],
        ),
    ]