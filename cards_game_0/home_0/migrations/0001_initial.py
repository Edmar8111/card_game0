# Generated by Django 5.0.6 on 2024-09-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=50)),
                ('image_card', models.ImageField(upload_to='image_cards')),
            ],
        ),
    ]
