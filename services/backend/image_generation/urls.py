
from django.urls import path
from .views import home, generate_images,batch_images_view, previous_batches_view

urlpatterns = [
    path('', home, name='home'),
    path('generate-images/', generate_images, name='generate_images'),
    path('batch-images/<int:batch_id>/', batch_images_view, name='get_batch_images'),
    path('previous-batches/', previous_batches_view, name='previous_batches'),
]
