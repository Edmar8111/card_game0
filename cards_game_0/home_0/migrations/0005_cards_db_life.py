# Generated by Django 5.1.1 on 2024-09-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_0', '0004_cards_db_verso_card_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards_db',
            name='life',
            field=models.IntegerField(default=100),
        ),
    ]
