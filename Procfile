web : gunicorn 'config.wsgi'
web: gunicorn config.wsgi --log-file -
#or works good with external database
web: python manage.py migrate && gunicorn config.wsgi
