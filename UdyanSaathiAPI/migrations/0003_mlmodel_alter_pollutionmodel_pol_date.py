# Generated by Django 4.2.6 on 2023-12-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UdyanSaathiAPI', '0002_alter_aqicalendarmodel_pol_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Station', models.CharField(default=' ', max_length=255)),
                ('Day1', models.FloatField(default=0, max_length=10)),
                ('Day2', models.FloatField(default=0, max_length=10)),
                ('Day3', models.FloatField(default=0, max_length=10)),
                ('Day4', models.FloatField(default=0, max_length=10)),
                ('Day5', models.FloatField(default=0, max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='pollutionmodel',
            name='Pol_Date',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]
