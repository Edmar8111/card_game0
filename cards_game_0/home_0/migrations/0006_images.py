# Generated by Django 5.1.1 on 2024-09-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_0', '0005_cards_db_life'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='image_0')),
            ],
        ),
    ]
