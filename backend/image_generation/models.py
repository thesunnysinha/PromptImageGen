from django.db import models

def image_upload_to(instance, filename):
    return f'images/batch_{instance.batch.id}/{filename}'

class Batch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Batch {self.id} - Created at {self.created_at}"

class Image(models.Model):
    batch = models.ForeignKey(Batch, related_name='images', on_delete=models.CASCADE)
    prompt = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return f"Image for prompt '{self.prompt}' in Batch {self.batch.id}"
