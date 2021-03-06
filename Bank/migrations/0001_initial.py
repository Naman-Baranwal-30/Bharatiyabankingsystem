# Generated by Django 3.2.5 on 2021-07-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('bal', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='transcations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('amt', models.IntegerField(max_length=100)),
                ('dt', models.DateTimeField()),
            ],
        ),
    ]
