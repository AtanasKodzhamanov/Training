# the command migrate makes changes to the database

# Commands
# django-admin startproject name
# python manage.py createsuperuser
# python manage.py makemigrations (do after writing a model)
# python manage.py migrate - will apply the migrations
# python manage.py shell - opens django shell 
    # from notes.models import Notes - imports table and you can the do manipulations/queries on it
    # mynote=Notes.objects.get(pk="1")
    # mynote.title
    # mynote.text
    # Notes.objects.all()
# python manage.py runserver

'''

Steps

Create your project and apps. 
Move apps within your main folder.
Set up settings: 
    - add installed apps 
    - add postgre database
    - add staticfiles folder 
Create urls.py file in each app and link to the templates 
Update main urls 
Update views to render templates 

'''