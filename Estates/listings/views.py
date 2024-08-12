from .models import  Property
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status
from listings.models import Property
from rest_framework.response import Response
from .serializers import PropertyFavoriteSerializer, PropertySerializer
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics



# Create your views here.



@permission_classes([IsAuthenticated])       # WORKES
class PropertyList(APIView):
    
    def get(self,request):
       
       properties= Property.objects.all()
       serializer= PropertySerializer(properties , many=True)

       return Response(serializer.data , status=status.HTTP_200_OK)

 
@permission_classes([IsAuthenticated])        # WORKES
class CreateProperty(APIView):
    
    def post(self,request):
       serializer= PropertySerializer(data=request.data)

       if not serializer.is_valid():
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      #  validated_data= serializer._validated_data
      #  serializer.create(validated_data)
       serializer.save(user=request.user)              # FIXED THE USER-PROPERTY RELATIONSHIP PRBLM
       return Response(serializer.data , status=status.HTTP_201_CREATED)




@permission_classes([IsAuthenticated])        # WORKES 
class RentPropertiesView(APIView):
   

    def get(self, request):

  
          
        rent_properties = Property.objects.filter(listing_type__iexact='rent') # Filter properties where listing_type is 'rent' (case insensitive)

        if not rent_properties.exists():  # Check if the queryset is empty
            return Response({'message': 'No rental properties found.'}, status=status.HTTP_404_NOT_FOUND)
        

        serializer = PropertySerializer(rent_properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    


class BuyPropertiesView(APIView):             # WORKES 
    permission_classes = [IsAuthenticated]

    def get(self, request):

            
        buy_properties = Property.objects.filter(listing_type__iexact='buy') # Filter properties where listing_type is 'buy' (case insensitive)

        if not buy_properties.exists():  # Check if the queryset is empty
            return Response({'message': 'No properties available for purchase.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PropertySerializer(buy_properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   



@permission_classes([IsAuthenticated])        # WORKES
class PropertyDetails(APIView):
   
   def get(self,request,pk):
      property= Property.objects.get(id=pk)
      serializer=PropertySerializer(property)

      return Response(serializer.data , status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])         # WORKES with user permissions
class UpdateProperty(APIView):

   def get(self,request,pk):
      property= Property.objects.get(id=pk)
      serializer=PropertySerializer(property)

      return Response(serializer.data , status=status.HTTP_200_OK)
   

   def put(self,request,pk):
      
      property= Property.objects.get(id=pk)
      serializer = PropertySerializer(property)

      if property.user != request.user:
            return Response({'detail': 'You do not have permission to edit this property.'}, status=status.HTTP_403_FORBIDDEN)
      
      serializer=PropertySerializer(data=request.data)
      
      if not serializer.is_valid():
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      validated_data= serializer._validated_data
      serializer.update(property, validated_data)

      return Response(serializer.data , status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])      # WORKES with user permissions
class DeleteProperty(APIView):

   def get(self,request,pk):
      property= Property.objects.get(id=pk)
      serializer=PropertySerializer(property)

      return Response(serializer.data , status=status.HTTP_200_OK)
   

   def delete(self,request,pk):
        property= Property.objects.get(id=pk)
        serializer = PropertySerializer(property)

        if property.user != request.user:
            return Response({'detail': 'You do not have permission to edit this property.'}, status=status.HTTP_403_FORBIDDEN)
      
        Property.objects.filter(id=pk).delete()

        return Response( 
        {'success':'property deleted successfully'}
         , status=status.HTTP_204_NO_CONTENT)




@permission_classes([IsAuthenticated])         # WORKS 
class MyListings(APIView):
   def get(self, request):
        mylistings = Property.objects.filter(user=request.user)
        serializer = PropertySerializer(mylistings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   

@permission_classes([IsAuthenticated])         # WORKS
class FavouritesView(APIView):


    def post(self, request, pk):
        # Get the property object
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response({'error': 'Property does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the property is already favorited
        if request.user in property.favourites.all():
            # If already favorited, remove it
            property.favourites.remove(request.user)
            return Response({'success': 'Property removed from favourites'}, status=status.HTTP_200_OK)
        else:
            # If not favorited, add it
            property.favourites.add(request.user)
            return Response({'success': 'Property added to favourites'}, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])         #WORKS
class MyFavouritesView(APIView):

    def get(self, request):
      try:
            
          user = request.user
          favourites = user.favourites.all()  # Get all properties that the user has favorited
          serializer = PropertyFavoriteSerializer(favourites, many=True)
          return Response(serializer.data, status=status.HTTP_200_OK)
      
      
      except Property.DoesNotExist:
            return Response({'error': 'Property does not exist.'}, status=status.HTTP_404_NOT_FOUND)
      

@permission_classes([IsAuthenticated])          #WORKS   
class PropertyFilterListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'squarft': ['lt'],
        'num_beds': ['exact'],
        'num_baths': ['exact'],
        'price': ['lt'], 

    }

    
    def list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())

            if not queryset.exists():  # Check if the queryset is empty
                return Response({'message': 'No properties found matching the specified requirments.'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
