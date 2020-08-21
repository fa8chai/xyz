# xyz

how to run:
pip install -r requirements.txt
python manage.py makemigrations users,
python manage.py makemigrations user_profile,
python manage.py migrate,
python manage.py createsuperuser and go to admin, add new school objects
in project/project/settings:
set PHONENUMBER_DEFAULT_REGION in order to know which national number format
to recognize. The setting is a string containing an ISO-3166-1 two-letter country code.
