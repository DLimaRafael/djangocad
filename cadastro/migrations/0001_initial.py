# Generated by Django 4.1.2 on 2022-10-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField()),
                ('senha', models.TextField(blank=True)),
                ('nasc', models.DateField()),
            ],
        ),
    ]
