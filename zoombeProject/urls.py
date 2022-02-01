from django import views
from django.contrib import admin
from django.urls import path,include

import website
import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('', include('user.urls')),

]