from django.urls import path
from . import views

app_name='reviews'

urlpatterns = [
    path('place_review',views.place_review,name='place_review'),
]
