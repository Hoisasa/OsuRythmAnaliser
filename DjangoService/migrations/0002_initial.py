# Generated by Django 4.2.13 on 2024-07-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DjangoService', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='non specified', max_length=30)),
                ('author', models.CharField(default='non specified', max_length=202)),
                ('lang', models.CharField(default='non specified', max_length=20)),
                ('bpm', models.IntegerField()),
            ],
        ),
    ]
