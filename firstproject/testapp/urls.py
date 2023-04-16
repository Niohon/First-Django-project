from django.urls import path
from .views import *

urlpatterns = [
    path('testapp/<int:testid>/', numbers),
    path('', index_page),

]
