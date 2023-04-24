from django.urls import path
from .views import *

urlpatterns = [
    path('testapp/<int:year>/', numbers),
    path('', index_page, name='home'),
    path('delete/', delete_all_workers),
    path('about/', about, name='about'),

]
