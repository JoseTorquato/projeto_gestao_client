# Generated by Django 3.1.5 on 2021-01-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=2)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bio', models.TextField(max_length=500)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cliente_photos')),
            ],
        ),
    ]
