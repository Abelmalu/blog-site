
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import global_settings

from Smart_Class_Room import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls') ),
    path('signup/',include('accounts.urls') ),

   
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

