# FakeDataCreationDjango

Django
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 

If you're just getting started, here's how we recommend you read the docs:

First, read docs/intro/install.txt for instructions on installing Django.
Next, work through the tutorials in order (docs/intro/tutorial01.txt, docs/intro/tutorial02.txt, etc.).

If you want to set up an actual deployment server, read docs/howto/deployment/index.txt for instructions.

You'll probably want to read through the topical guides (in docs/topics) next; from there you can jump to the HOWTOs (in docs/howto) for specific problems, and check out the reference (docs/ref) for gory details.
To run Django's test suite:

Follow the instructions in the "Unit tests" section of docs/internals/contributing/writing-code/unit-tests.txt, published online at https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests

To Create Custom Management command:

Check out https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/ for information anout getting involved.

{{ project_name|title }} Django Project
Prerequisites
python >= 2.5

pip

virtualenv/wrapper (optional)

Installation
Creating the environment

Create a virtual python environment for the project. If you're not using virtualenv or virtualenvwrapper you may skip this step.

For virtualenvwrapper

mkvirtualenv --no-site-packages {{ project_name }}-env

virtualenv --no-site-packages {{ project_name }}-env

cd {{ project_name }}-env

cd {{ project_name }}

cd {{ project_app }}-env

cd {{ project_app }}


Open settings file in Project and mention app name in Installed apps.

Do, required changes in urls.py and views.py 
 
Running:

python manage.py runserver

Open browser to http://127.0.0.1:8000
 

Create models as follows based on your requirements:

from django.db import models

# Create your models here.

class users(models.Model):
    id = models.IntegerField(primary_key=True);
    real_name = models.CharField(max_length=100);
    tz = models.CharField(max_length=100);
    activity_periods = models.TimeField(auto_now=True);
    start_time = models.DateTimeField();
    End_time = models.DateTimeField();




Do,  required changes in admin.py and if you are using static files which are html and css files create a template folder in a project and add template directory in settings.
After the changes run the following commands:

Python manage.py makemigrations

Python manage.py migrate 

Create Super_user in cmd by using particular commands such as

Python manage.py create superuser
Fill the required details and your account is created successfully. 

Create super_user and login with the same details to the django admin.

In Html file write jinja2 code to display the particular columns of data in django admin.

Create fake data using faker.
Installation:

Pip install faker

Create object as

Import faker as Faker

fake = Faker()

Using fake we can call any fake name, address, country, date, time and required fake data.
Eg:
fake.id()
fake.name()

All the fake data code should be written in .py file in project.

Run the fake object code file using the following command in cmd file.

Python filename.py
 



