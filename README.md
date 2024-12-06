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
    from django.contrib.auth.decorators import login_required

    # Create your views here.
    
    def index(request):
        return render(request,'auth_app/index.html')

    def home(request):
        return render(request,'auth_app/home.html')
    @login_required
    def login(request):
        return render(request, 'auth_app/login.html')

16. creo en templates/auth_app/home.html

    ```bash
   <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body class="bg-light">
        <div class="container mt-5">
            <h1 class="text-center">Welcome to Home Page</h1>
            <p class="text-center"><a href="{% url 'login' %}" class="btn btn-primary">Login</a></p>
            <p class="text-center"><a href="{% url 'index' %}" class="btn btn-primary">Index</a></p>

        </div>
    </body>

    </html>
17. templates/auth_app/index.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body class="bg-light">
        <div class="container mt-5">
            <h1 class="text-center">index HTML</h1>
            {% if user.is_authenticated %}
            <h2>Usuario autenticado</h2>
            <p class="text-center">Hello, {{ user.username }}!</p>
            <form method="post" action="{% url 'logout' %}" class="text-center">
                {% csrf_token %}
                <button type="submit" class="btn btn-danger">Logout</button>
            </form>
            {% else %}
            <h2>No tiene permisos para ver esta página</h2>
            <p class="text-center"><a href="{% url 'login' %}" class="btn btn-primary">Login</a></p>
            {% endif %}
        </div>
    </body>

    </html>
18. templates/auth_app/login.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>

    <body class="bg-light">
        <div class="container mt-5">
            <h1 class="text-center mb-4">Login</h1>
            <div class="card p-4 shadow-sm">
                <form method="post">
                    {% csrf_token %}
                    {{ form.as_p }}
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
            </div>
        </div>
    </body>
    </html>

19. Necesito configurar el url, en auth_project voy a urls.py
     ```bash
    from django.contrib import admin
    from django.urls import path,include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('auth_app.urls')),
    ]

20. En auth_app / creo la urls.py
     ```bash
    from django.urls import path
    from django.contrib.auth import views as auth_views
    from .import views

    urlpatterns = [
        path('login/',auth_views.LoginView.as_view(template_name='auth_app/login.html'), name="login"),
        path('logout/',auth_views.LogoutView.as_view(), name="logout"),
        path('',views.index,name='index'),
        path('home/',views.home,name='home'),
    ]
21. Me logeo a través de página http://127.0.0.1:8000/admin
     ```bash
     admin
     admin1234

22. Ingreso al auth_project/settings.py
    ```bash
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.1/howto/static-files/

    STATIC_URL = 'static/'

    LOGIN_REDIRECT_URL = '/'
    LOGOUT_REDIRECT_URL = '/home'
