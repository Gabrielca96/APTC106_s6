# simple-crud-django
Simple CRUD con django, utilizando vistas basadas en funciones y autentificacion 


1. Crear entorno virtual `virtualenv nombre-entorno`
2. Instalar dependecias: `pip install -r requierements.txt`
3. Realizar migraciones `python manage.py makemigrations && python manage.py migrate`
4. Correr servidor `python manage.py runserver`


# Crear usuario por consola

- doc create super user: https://docs.djangoproject.com/en/5.0/topics/auth/default/
 
- command: python3.8 manage.py createsuperuser --username=gcampos --email=gabriel.campos.aburto@gmail.com

# Errores encontrados

- Error con zlib:
    - sudo apt-get install libjpeg-dev zlib1g-dev