# plateforme
I-) changement de la base de donnée
~~~~~~~~  1  ~~~~~~~~~~
python manage.py dumpdata > db.json
~~~~~~~~  2  ~~~~~~~~~

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'plateformDB',
	"USER": 'root',
	"PASSWORD": '';
	"HOST": 'localhost',
	"PORT": '3306',
	# default-character-set = utf8
    }
}

~~~~~~~  3  ~~~~~~~~~~~
python manage.py makemigration
~~~~~~~  4  ~~~~~~~~~~
python manage.py migrate
~~~~~~~  5  ~~~~~~~~~~
python manage.py shell
~~~~~  6  ~~~~~~~~~~~~
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>>exit()
~~~~~~   7  ~~~~~~~~~~~
python manage.py loaddata db.json
