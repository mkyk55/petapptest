from django.urls import path
from .views import *
urlpatterns = [
    path('', view=homepage ,name='home'),
    path('login', view=login ,name='login'),
    path('logout', view=logout ,name='logout'),
    path('dogs', view=dogs ,name='dogs'),
     path('trainedgerman', view=trainedgerman ,name='trainedgerman'),
]