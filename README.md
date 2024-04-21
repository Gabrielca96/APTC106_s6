# simple-crud-django
Simple CRUD con django, utilizando vistas basadas en funciones y autentificacion 


1. Crear entorno virtual `python3.8 -m venv venv`
2. Activar entorno virtual linux `source venv/bin/activate`
2. Instalar dependecias: `pip install -r requierements.txt`
3. Realizar migraciones `python3.8 manage.py makemigrations && python manage.py migrate`
4. Correr servidor `python3.8 manage.py runserver`

# Administracion de usuarios

## Crear usuario por consola

- doc create super user: https://docs.djangoproject.com/en/5.0/topics/auth/default/
 
- command: `python3.8 manage.py createsuperuser --username=gcampos --email=gabriel.campos.aburto@gmail.com`

## Eliminar usuario por consola

1. `python3.8 manage.py shell`

2. `from django.contrib.auth.models import User`

3. `User.objects.get(username="gcampos", is_superuser=True).delete()`

4. `exit()`

# Errores encontrados

- Error con zlib:
    - `sudo apt-get install libjpeg-dev zlib1g-dev`