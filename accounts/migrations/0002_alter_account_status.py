# Generated by Django 4.0.6 on 2022-07-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(choices=[('top', 'top'), ('satisfactory', 'satisfactory'), ('unsatisfied', 'unsatisfied')], default=None, max_length=32),
        ),
    ]
