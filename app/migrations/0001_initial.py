# Generated by Django 4.2 on 2023-04-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100)),
                ('productprice', models.IntegerField(max_length=100)),
                ('productquantity', models.IntegerField()),
            ],
        ),
    ]
