# Generated by Django 3.0.5 on 2021-05-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('branch', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
