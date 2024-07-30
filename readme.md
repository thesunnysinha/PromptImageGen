### Prerequisites

1. **Create `.env` File inside backend Folder:**

    Create a `.env` file in your project directory using `envExample` as a template. Ensure it includes the following configuration:

    ```
    STABILITY_API_KEY=your_stability_ai_api_key_here
    ```

    Replace `your_stability_ai_api_key_here` with the API key obtained from Stability AI.

2. **Install Redis:**

    ### For Linux
    ```
    sudo apt update
    sudo apt install redis-server
    sudo systemctl start redis-server
    sudo systemctl enable redis-server
    sudo systemctl status redis-server
    ```

3. **Create and Activate Virtual Environment:**

   Open Command Prompt (cmd) and navigate to your project directory.

   Create a virtual environment named `venv`:

   ```
   python -m venv venv
   ```

   Activate the virtual environment:
   
   ```
   venv\Scripts\activate
   ```


4. **Install Dependencies:**

 While inside the activated virtual environment, install dependencies from `requirements.txt`:

 ```
 cd backend
 pip install -r requirements.txt
 ```

### Using Script

1. **Run `runserver.sh` Script:**

 Make the script executable:

 ```
 chmod +x runserver.sh
 ```

 Execute the script:

 ```
 ./runserver.sh
 ```
 
 This script performs the following actions:
 - Deletes unwanted `pycache` and `migrations` folders from the project.
 - Runs migrations for the `image_generation` app.
 - Sets up the application, including migrating the database and creating a superuser.
 - Username: admin
 - Password: admin@123
 - Starts the Django development server.

### Celery Worker Script

2. **Run `celery_worker_script.sh` Script:**

 Make the script executable:

 ```
 chmod +x celery_worker_script.sh
 ```

 Execute the script:

 ```
 ./celery_worker_script.sh
 ```

 This script starts the Celery worker for asynchronous task processing.

### Manually

1. **For Django Server**

 ```
 cd backend
 python manage.py migrate
 python manage.py makemigrations
 python manage.py runserver 0.0.0.0:8000
 ```

2. **For Celery Worker**

 ```
 cd backend
 celery -A main worker --loglevel=info -c 6
 ```

 Replace `6` with the number of workers you want to run.


### Functionalities

1. **Generate Images from Multiple Prompts**: Users can add multiple prompts from the frontend and generate images for all of them simultaneously. After the generation process is complete, a modal will open displaying the images in a carousel format.

2. **Batch Saving**: Generated images are saved in batches on the backend for efficient management.

3. **View Previous Batches**: Users can access previously generated batches by clicking on the "View Previous Batches" option.

4. **View Batch Images**: Clicking "View Previous Batches" will open a modal with all previously generated batches. Users can select an image link to open another modal that displays the images from that batch in a carousel. Navigation options allow users to view the next or previous image, with the corresponding prompt displayed at the bottom.


### Samples

1. ***Home***

    ![Home](./samples/home.png)

3. ***Generated Image for prompt A Red flying Dog***

    ![Generated Image](./samples/generated_image.png)


2. **Previous Batches***
    ![Previous Batches](./samples/previous_batches.png)


