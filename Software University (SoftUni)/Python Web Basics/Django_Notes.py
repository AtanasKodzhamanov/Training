# the command migrate makes changes to the database

# Commands
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