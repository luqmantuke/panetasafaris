# Generated by Django 3.1.1 on 2021-07-13 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_auto_20210713_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('tour_name', models.CharField(max_length=255, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('message', models.TextField(blank=True, null=True)),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='destinations.destination')),
            ],
        ),
    ]
