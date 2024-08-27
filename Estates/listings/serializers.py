from rest_framework.serializers import ModelSerializer

from accounts import serializers
from .models import Property

class PropertySerializer(ModelSerializer):
   class Meta :
      model = Property
      fields = '__all__' #['id', 'user, ''address', 'num_beds', 'num_baths', 'squarft', 'contact_num', 'description', 'price','image','image1','image2']
      read_only_fields = ('user',)  # Make user field read-only


class PropertyFavoriteSerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'address', 'price', 'num_beds', 'num_baths', 'squarft', 'contact_num', 'description', 'squarft', 'image', 'image1','image2', 'listing_type']
