# Generated by Django 5.0.1 on 2024-01-28 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count_cooked', models.ImageField(default=0, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MassProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mass_product', models.ImageField(upload_to='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_food.product')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('mass_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_food.massproduct')),
                ('product_id', models.ManyToManyField(to='recipe_food.product')),
            ],
        ),
    ]