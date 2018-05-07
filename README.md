# django-test
django-test

To Create virtualenv

```
virtualenv -p python3 .
```

To Activate virtualenv

```
source bin/activate
```

Then

```
mkdir src && cd src
```

To Activate virtualenv

```
sudo pip install Django==1.11
```
```
django-admin startproject django-test .
```

To run server

```
python manage.py runserver
```

To migrate

```
python manage.py migrate
```

To Create super user

```
python manage.py createsuperuser

```

To collect static

```
python manage.py collectstatic
```

To make an apps

```
python manage.py startapp products
```

Every single time when you make change your models. run

```
python manage.py makemigrations
```
```
python manage.py migrate
```