# Install Django
pip install django

# Install Django REST Framework
pip install djangorestframework

django-admin startproject alxtravelapp
cd alxtravelapp

python manage.py runserver

pip install mysqlclient

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',  # Replace with your MySQL database name
        'USER': 'your_db_user',  # Replace with your MySQL username
        'PASSWORD': 'your_db_password',  # Replace with your MySQL password
        'HOST': 'localhost',  # If MySQL is hosted locally, else replace with your host (e.g., '127.0.0.1' or a cloud provider)
        'PORT': '3306',  # Default MySQL port
    }
}

python manage.py migrate

pip install django-environ

pip install django-cors-headers
