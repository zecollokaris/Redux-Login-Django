# <p align="center"> DJANGO LOGIN <p>

# DESCRIPTION

A Simple Django Application Providing User Registration Functionality using Redux Registration Process for Django Websites.

# REDUX DEFINITION

Redux is a predictable state container designed to help you build apps that behave consistently across client, server, and native environments and are easy to test.

Redux implements many performance optimizations internally so that your own connected component only rerenders when it actually needs to.

# SET UP

1. Install django-registration-redux

```
pip install django-registration-redux
```

2. Add registration in to your INSTALLED_APPS

#### `settings.py`

```
INSTALLED_APPS = [
    ....
    'registration',
    ....
    ]
```

#### `settings.py`

```
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
```

3. Migrate for registration tables to be created in the database

```
python manage.py migrate
```

4. Add a url to include urls from registration app you just installed

#### `urls.py`

```
    # REGISTRATIION PAGE Url Pattern!

    path('accounts/', include('registration.backends.default.urls')),
```

Users would then be able to register by visiting the URL ```/accounts/register/``` login (once activated) at ```/accounts/login/```.

5. In your template folder, make a template page and name it base.html

#### `base.html`

```
{% load i18n %}

{% trans "Log in" %}
{%load bootstrap4 %}
{% load static %}
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title> Django Login</title>

    {%block styles%}
    {%bootstrap_css%}
    <link rel="stylesheet" href="{% static 'css/management.css' %}">
    <link rel="stylesheet" href="{% static 'css/navbar.css' %}">
    {% endblock %}
</head>
<body style="margin-top: 300px; margin-left: 40%;" >
{% include 'Success/nav.html' %}
{%block content%} 
<form method="post" action="">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="{% trans 'Log in' %}" />
    <input type="hidden" name="next" value="{{ next }}" />
</form>

<p>{% trans "Forgot your password?" %} <a href="{% url 'auth_password_reset' %}">{% trans "Reset it" %}</a>.</p>
<p>{% trans "Not a member?" %} <a href="{% url 'registration_register' %}">{% trans "Register" %}</a>.</p>

{% endblock %}
{% block scripts %}


<script src="{% static 'js/App.js' %}"></script> 
{% bootstrap_javascript %} 
{% endblock %}
</body>
</html>
```

6. Import login required decorator and place them above all views that needs login before accessing.


```
from django.contrib.auth.decorators import login_required

#Home page view function
@login_required
def index(request):
	title = 'Welcome: This is the Home Page'
	context = {
	    "title": title,
	}
	return render(request, "Success/index.html",context)
```

This restricts site to unauthenticated users and redirects them to login page when they try access the restricted url

7. Login to the app through this url: ```/accounts/login```

    Logout URL is: ```/accounts/logout```

# Prerequisites

# Setup/Installation Reqiurements.
**{follow the below instructions for set up.}**

# Technologies Used

# Support and Contact

-Mobile number: (+254) 798731203

-Email Address: collo.kariss@gmail.com

-github-username: zecollokaris

## License

The app is licensed by MIT.

Collins Kariuki - MIT (c)2018 LICENSE



