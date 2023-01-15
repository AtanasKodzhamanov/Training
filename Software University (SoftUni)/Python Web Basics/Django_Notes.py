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

django-admin startproject myproject

Move to the project folder and create an app:
    python manage.py startapp myapp

Should have the following structure:
    myproject
        manage.py
        myproject
            settings.py
            webapp
                views.py
        staticfiles
        templates

Then add the app to the installed apps in settings.py
    'myproject.myapp',

Then add the app to the urls.py in the project folder
    path("", include("myproject.myapp.urls")),

Go to settings and add database connection. 
    python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


'''