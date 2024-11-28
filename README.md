<!-- reset the database -->

rm db.sqlite3

<!-- recreate migrations and apply them -->

python manage.py makemigrations
python manage.py migrate
