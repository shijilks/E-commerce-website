# Generated by Django 5.0 on 2023-12-31 10:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default='')),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('kerala', 'kerala'), ('Goa', 'Goa'), ('Delhi', 'Delhi'), ('Gujart', 'Gujart'), ('Tamil Nadu', 'Tamil Nadu'), ('Mumbi', 'Mumbi'), ('kolakatta', 'Kolatta'), ('Pune', 'Pune')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
