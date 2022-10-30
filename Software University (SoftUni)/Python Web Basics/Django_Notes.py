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

1. Create your project and apps. 
2. Move apps within your main folder.
3. Set up settings: 
    - add installed apps 
    - add postgre database
    - add staticfiles folder 
4. Create urls in each app and link to the templates 
5. Update main urls 
6. Update views to render templates 

'''