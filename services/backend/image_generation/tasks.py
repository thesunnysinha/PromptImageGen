from celery import shared_task
import requests
from django.core.files.base import ContentFile
from .models import Batch, Image
import io
from django.conf import settings

@shared_task
def generate_image(prompt, batch_id):
    api_url = 'https://api.stability.ai/v2beta/stable-image/generate/sd3'
    headers = {
        'authorization': f'Bearer {settings.STABILITY_API_KEY}',
        'accept': 'image/*'
    }

    data = {
        'prompt': prompt,
        'output_format': 'jpeg'
    }

    try:
        # Make the API request
        response = requests.post(api_url, headers=headers, files={"none": ''}, data=data)
        response.raise_for_status()

        if response.status_code == 200:
            # Retrieve or create the Batch instance
            batch, created = Batch.objects.get_or_create(id=batch_id)

            # Prepare image content for saving
            image_content = io.BytesIO(response.content)
            image_file = ContentFile(image_content.read(), name=f'{batch_id}_{prompt[:10]}.jpeg')

            # Create the Image instance
            Image.objects.create(
                batch=batch,
                prompt=prompt,
                image=image_file
            )

            return {'prompt': prompt, 'status': 'Image saved successfully'}

        else:
            error_message = response.json().get('error', 'Unknown error')
            raise ValueError(f"API Error: {error_message}")

    except requests.RequestException as e:
        return {'prompt': prompt, 'error': f"Request error: {str(e)}"}

    except ValueError as e:
        return {'prompt': prompt, 'error': f"Value error: {str(e)}"}

    except Exception as e:
        return {'prompt': prompt, 'error': f"An error occurred: {str(e)}"}
