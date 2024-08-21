# Generated by Django 4.2.6 on 2023-10-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_driver_reg_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('Password', models.CharField(max_length=30)),
                ('Cnf_password', models.CharField(max_length=30)),
            ],
        ),
    ]
