# Generated by Django 3.1.1 on 2020-09-17 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='DEFAULT VALUE', max_length=300, null=True)),
                ('mr_no', models.IntegerField(blank=True, default='DEFAULT VALUE', null=True)),
                ('room_no', models.IntegerField(blank=True, default='DEFAULT VALUE', null=True)),
                ('Diagnosis', models.CharField(blank=True, default='DEFAULT VALUE', max_length=300, null=True)),
                ('Consultant', models.CharField(blank=True, choices=[('AK', 'Ahmed Elshahat Kabil'), ('KH', 'Khaled AlAbdi')], max_length=300, null=True)),
                ('tt_is_there', models.BooleanField(blank=True, default=False)),
                ('tt_insert_date', models.DateField(blank=True, default=datetime.date(2020, 9, 17))),
                ('tt_type', models.CharField(blank=True, choices=[('TR', 'Traco'), ('SE', 'Something Else')], max_length=300, null=True)),
                ('tt_size', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('tt_due_date', models.DateField(blank=True, default=datetime.date(2020, 12, 10))),
                ('peg_is_there', models.BooleanField(blank=True, default=False)),
                ('peg_insert_date', models.DateField(blank=True, default=datetime.date(2020, 9, 17))),
                ('peg_size', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
        ),
    ]
