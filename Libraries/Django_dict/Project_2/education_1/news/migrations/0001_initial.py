# Generated by Django 4.2.7 on 2023-12-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Стаття')),
                ('date', models.DateTimeField(verbose_name='Дата публікації')),
            ],
        ),
    ]
