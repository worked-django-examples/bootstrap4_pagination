# Generated by Django 4.0.5 on 2022-07-04 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AnnualPopulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('population', models.IntegerField(null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.country')),
            ],
        ),
    ]
