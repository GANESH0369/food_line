# Generated by Django 4.2 on 2023-04-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employesviws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('empid', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('m_number', models.IntegerField()),
            ],
        ),
    ]
