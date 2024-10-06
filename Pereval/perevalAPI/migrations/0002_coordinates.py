# Generated by Django 5.1 on 2024-10-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevalAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('height', models.IntegerField(null=True)),
            ],
        ),
    ]
