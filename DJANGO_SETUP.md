#instructions for django project setup

1. create the django project

    django-admin startproject <nameofproject>

2. create the apps directory
    
    cd <nameofproject>

    mkdir apps
  
    cd apps

3. create the dunder file

    touch __init__.py

4. create the django app

    python ../manage.py startapp first_app

5. add the app to settings.py

   add to INSTALLED_APPS as apps.<whatever app is called>

6. create the route app

   # mod the primary urls.py file to include the application

      # i.e.
```
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('apps.myapp.urls'))
] 
```
### mod the urls.py file in the actual application (create it first) and label view.<method you want to fire on that path>

```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index)
]
```
7. create the view methods, create the views you want to fire for the app routes
```
def index(request):

    context = {
        "word":"stuff"
    }
    return render(request, 'myapp/index.html', context)
```
8. build templates and static folders

    cd into your new app dir

    mkdir templates static

    create a folder called the name of app in templates and static files

    add img, js, css dir to static/name of app 

9. activate and use session in django
```
python manage.py makemigrations
python manage.py migrate
```
only use dot notation to get session vars, bracket notation to set 

10. apply csrf tokens in forms
```
{% csrf_token %}   
```
 
