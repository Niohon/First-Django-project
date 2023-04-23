"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
# import sys
# import pprint

# sys.path.append('D:\\Python\\First django project\\firstproject\\testapp')
# pprint.pprint(sys.path)

# import os
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')
# django.setup()

from django.contrib import admin
from django.urls import include, path

from firstproject import settings
from testapp.views import pageNotFound

urlpatterns = [
    path('', include('testapp.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler404 = pageNotFound
