import json
import uuid
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Batch, Image
from .tasks import generate_image
from celery import group

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    

def previous_batches_view(request):
    if request.method == 'GET':
        batches = Batch.objects.all()
        batch_results = []

        for batch in batches:
            prompts = batch.images.all().values('prompt')
            batch_results.append({
                'batch_id': batch.id,
                'prompts': list(prompts)
            })
            
        return render(request, 'previous_batches.html', {'batches': batch_results})

@csrf_exempt
def generate_images(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompts = data.get('prompts', [])
            
            if len(prompts) == 0:
                return JsonResponse({'error': "Prompts are empty."}, status=400)

            batch = Batch.objects.create()

            task_group = group(generate_image.s(prompt, batch.id) for prompt in prompts)
            task_group.apply_async().get()

            if not Image.objects.filter(batch=batch).exists():
                batch.delete()
                return JsonResponse({'error': 'Failed to generate images'}, status=500)
            
            return JsonResponse({
                'batch_id': batch.id
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def batch_images_view(request, batch_id):
    if request.method == 'GET':
        try:
            batch = Batch.objects.get(id=batch_id)
            images = batch.images.all()
            image_data = [
                {
                    'prompt': image.prompt,
                    'image_url': image.image.url
                }
                for image in images
            ]
            return JsonResponse({'images': image_data})
        except Batch.DoesNotExist:
            return JsonResponse({'error': 'Batch not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=405)