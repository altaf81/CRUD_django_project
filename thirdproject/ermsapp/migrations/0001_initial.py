# Generated by Django 4.0.1 on 2022-02-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_salary', models.FloatField()),
            ],
        ),
    ]