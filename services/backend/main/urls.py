
from django.contrib import admin
from django.urls import path,include
from image_generation import urls as image_generation_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


########### Image Generation #########

urlpatterns += [
    path("",include(image_generation_urls))
]