# Generated by Django 5.0.4 on 2024-05-06 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Nazvanie kategorii')),
                ('image', models.ImageField(upload_to='cat_img/', verbose_name='kartinka kategorii')),
                ('slug', models.SlugField(unique=True, verbose_name='Ssilka')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategorii',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Novost', 'verbose_name_plural': 'Novosti'},
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]