from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^volume/volume/$', 'volume.views.volume'),
    url(r'^keyboard/click/$', 'keyboard.views.click'),
]