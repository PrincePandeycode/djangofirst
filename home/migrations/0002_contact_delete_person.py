# Generated by Django 4.1.7 on 2023-03-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('addr', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
