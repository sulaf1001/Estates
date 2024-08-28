from django.db import models
from Estate import settings
from accounts.models import UserAccount
from django.core.validators import MinValueValidator



# Create your models here.
class Property (models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address =models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    num_beds = models.IntegerField(validators=[MinValueValidator(0)])
    num_baths = models.IntegerField(validators=[MinValueValidator(0)])
    squarft = models.IntegerField(validators=[MinValueValidator(0)])
    contact_num =models.CharField(max_length=10,default="0000000000")
    description =models.TextField(max_length=2000, blank=True)
    favourites = models.ManyToManyField( UserAccount , related_name='favourites' , default= False , blank=True )
    image = models.ImageField(upload_to='images/', max_length=300)
    image1 = models.ImageField(upload_to='images/', max_length=300)
    image2 = models.ImageField(upload_to='images/', max_length=300)
    listing_type = models.CharField(max_length=100)
    approved= models.BooleanField(default= False)

    # uncomment to define the listing type as a list of options rather than charField .

    # LISTING_TYPES = (
    #     ('rent', 'Rent'),
    #     ('buy', 'Buy'),
    # )
    # listing_type = models.CharField(max_length=4, choices=LISTING_TYPES, default='rent')


    def __str__(self):
     return str(self.address)


