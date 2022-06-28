# Generated by Django 4.0.5 on 2022-06-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('foto', models.CharField(max_length=9999999)),
                ('tamanio', models.CharField(choices=[('1', 'Individual'), ('2', 'Grande'), ('3', 'Familiar')], max_length=20)),
                ('ingredientes', models.CharField(max_length=60)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]