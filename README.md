# M6-L8-Django-AutorizacionAutenticacion-
Educativo y de Aprendizaje Personal

# proyecto_tareas_django
Educativo y de Aprendizaje Personal

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activación del Entorno](#Activación-del-Entorno)
- [Configuración Inicial](#configuración-inicial)
- [Pasos del Proyecto](#pasos-del-proyecto)
  - [Creación del Superusuario](#Creación-del-Superusuario)
  - [Configuración del Proyecto](#configuración-del-proyecto)
  - [Creación de Vistas y Modelos](#creación-de-vistas-y-modelos)

---
## Requisitos

- Python 3.9 o superior
- Django 4.0 o superior

---
## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv entorno_virtual 

## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    entorno_virtual\Scripts\activate

## Configuración Inicial
## Instalar Django y Guardar dependencias

3. Intalación Django
    ```bash
    pip install django

4. Instalamos la actualizacion de pip
    ```bash
    python.exe -m pip install --upgrade pip

## Guardar las dependencias
5. Instalación dependencias
    ```bash
   pip freeze > requirements.txt

## Pasos del Proyecto
6. Crear el Proyecto
    ```bash
    django-admin startproject auth_project

7. Ingresar al directorio del Proyecto
    ```bash
    cd auth_project

8. Hacer las migraciones correspondientes y se va crear db.sqlite3
    ```bash
    python manage.py migrate

## Creación del superusuario
9. Creamos el super usuario , se refleja db.sqlite3 en auth_user , id , password, username
    ```bash
    python manage.py createsuperuser 

10. Por Motivos de aprendizaje y no de seguridad estas van hacer las credenciales 
    ```bash
    admin
    admin@gmail.com
    admin1234
    y

11. Activamos el servidor pero vamos a la siguiente ruta 127.0.0.1:8000/admin 
    ```bash
    python manage.py runserver

12. Creamos la Aplicación 
    ```bash
    python manage.py startapp auth_app

## Configuración del Proyecto

13. Conectar el proyecto con la aplicación: Agregar 'auth_app', en la lista INSTALLED_APPS dentro del archivo auth_project/settings.py

    ```bash
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auth_app',
    ]

14. crear dentro de la carpeta auth_app      templates/auth_app/home.html

### Creación de Vistas y Modelos

15. Necesito crear las vistas en auth_app/views.py 

    ```bash
    from django.shortcuts import render

    # Create your views here.
    def home(request):
        return render(request,'auth_app/home.html')

16. creo en templates/auth_app/home.html
  ```bash
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
    </head>

    <body>
        <h1>Soy el Home</h1>
    </body>

    </html>

17. Necesito configurar el url, en auth_project voy a urls.py
     ```bash
    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('auth_app.urls')),
    ]

18. En auth_app / creo la urls.py


