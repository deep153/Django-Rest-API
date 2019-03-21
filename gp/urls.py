
from django.contrib import admin
from django.conf.urls import include, url
from recipe import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('', include('recipe.urls')),
]
