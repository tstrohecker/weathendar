from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('weathendar_django.polls.urls')),
    path('admin/', admin.site.urls),
]