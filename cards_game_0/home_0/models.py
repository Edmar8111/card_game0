from django.db import models

# Create your models here.
class Cards_db(models.Model):
    name=models.CharField(max_length=50, default='None')
    image_card=models.ImageField(upload_to='image_cards')
    overhead = models.DecimalField(decimal_places=1, default=0, max_digits=5) 
    verso_card_img = models.ImageField(upload_to='image_cards')
    
