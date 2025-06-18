from django.urls import path
from . import views

app_name='reviews'

urlpatterns = [
    path('place_review',views.place_review,name='place_review'),
    path('google_v', views.google_v, name='google_v'),

]
