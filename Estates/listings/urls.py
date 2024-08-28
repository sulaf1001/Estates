from django.urls import path
from . import views

urlpatterns =[

path('properties/', views.PropertyList.as_view(), name='list_of_properties'),
path('create_property/', views.CreateProperty.as_view(), name='Create'),
path('delete_property/<int:pk>/', views.DeleteProperty.as_view(), name='Delete'),
path('update_property/<int:pk>/', views.UpdateProperty.as_view(), name='Update'),
path('properties/<int:pk>/', views.PropertyDetails.as_view(), name='property_details' ),
path('mylistings/',views.MyListings.as_view(),name='MyListings'),
# path('rent/', views.RentPropertiesView.as_view()),
# path('buy/', views.BuyPropertiesView.as_view()),
path('properties/<int:pk>/favourites/', views.FavouritesView.as_view(), name='favourites'),
path('myfavourites/', views.MyFavouritesView.as_view(), name='myfavourites'),
path('propertyFilter/', views.PropertyFilterListView.as_view(), name='cars-filter'),

]