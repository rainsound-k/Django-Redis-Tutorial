from django.contrib import admin
from django.urls import path

from posts.views import post_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_view),
]
