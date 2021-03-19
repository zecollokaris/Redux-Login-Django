# <p align="center"> :key: DJANGO LOGIN <p>



# DESCRIPTION

A Simple Django Application Providing User Registration Functionality using Redux Registration Process for Django Websites.

# REDUX DEFINITION

Redux is a predictable state container designed to help you build apps that behave consistently across client, server, and native environments and are easy to test.

Redux implements many performance optimizations internally so that your own connected component only rerenders when it actually needs to.

# DISPLAY

## Admin Page

<p align="center">
<img align="centre" src="Spec.md/admin.png" alt="Admin Page" />
<p>

## Login Page

<p align="center">
<img align="centre" src="Spec.md/login.png" alt="Login Page" />
<p>

## Reset Password Page

<p align="center">
<img align="centre" src="Spec.md/reset.png" alt="Reset Password Page" />
<p>

## Home Page

<p align="center">
<img align="centre" src="Spec.md/home.png" alt="Home Page" />
<p>


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

#  PREREQUISITES

- You need to have nano text editor installed. you can find out whether you have it installed by typing nano --version in your terminal. For most linux distributions, it is installed by default. However, if you don't have it installed, you can quicky do that by typing sudo apt-get install nano in your terminal.

- You need to have (python3.8) installed in your machine

- Python3.8. Installation ```$ sudo apt-get install python3.8```

- Django3.17. Installation ```$ pip install django==3.17```

- Psycopg2. Installation ```$ pip install psycopg2```

- Bootstrap4. Installation ```$ pip install django-bootstrap4```


# SETUP/INSTALLATION REQUIREMENTS.

**Follow The Below nstructions For Set Up.**

- Internet connection

- webpage URL:

- To get to this webpage fist you need to get to my github repository

- The link to my github Repository is: https://github.com/zecollokaris

- from there you can access the project

- git clone project.

- install dependancies in requirements.txt file ```$ pip install -r requirements.txt```

- cd into project

- create a virtual environment ```$ python3.6 -m venv virtual```

- Activate Virtual Environmrnt. ```$ source virtual/bin/activate```

- Run The Project-: ```$ python manage.py runserver```



# TECHNOLOGIES USED
- HTML5 

- CSS

- Bootstarap

- Python3.8

- Django 3.1.7

- Psycopg2 

- PostgreSQL


```
```

```
```

```
```

```
```


## 1. Give Examples Of Different Integration Protocols You Have Come Across And Give
## Example Scripts In Python 3 on How to Achieve Each One.

Application integration is the process of enabling independently designed applications to work together providing access to data and functionality from independently designed applications through what appears to be a single user interface or application service
With application integration, you can enter data once and connect it to multiple applications instead of entering the same data as many times as you have applications. When you add new data into an application that has been integrated with other applications, the data will be automatically distributed throughout the connected applications. This reduces human error, the need for manual intervention, and overall ensures consistency across your platforms.

Advantages of Integration.

- Speeds up company processes
- Increases work efficiency
- Ensures effective information exchanges
- Enables basic system operations.

The Major Types of Third-Party Integration Methods Are.

1. API (Application Programming Interface)
 An API uses a common code language to specify functionality and set protocols. This gives your applications the ability to transfer data.
 An example of a project Ive done that uses APIs is **[https://github.com/zecollokaris/Github-API-Search--Update-Angular-cli-7](https://github.com/zecollokaris/Github-API-Search--Update-Angular-cli-7)** that searches for user and displays their profile info on an Angular Application.


2. WEBHOOKS
For webhooks, implementation is often not code-based. They often have modules that are programmable within a web application. Instead of being request-based, webhooks are event-based. They only trigger when specific events occur within a third-party service.

3. ISC (Integration Services Component)
The ISC creates a bridge with on-premise tools such as directories, asset management tools, and BI tools without the need for file imports.

4. ORCHESTRATION
They refer to the process of automating multiple systems and services together. Teams will often use software configuration management tools such as PowerShell to build orchestrations.
 An example of a project Ive done that may give you some understanding of how orchestration works is **[https://github.com/zecollokaris/Flask-CLI](https://github.com/zecollokaris/Flask-CLI)** It helps in creating files needed in flask and this making it easy for you to code as you no longer have to create them on your own.

## 2. Give A Walkthrough Of How You Will Manage A Data Streaming Application Sending
## One Million Notifications Every Hour While Giving Examples Of Technologies And
## Configurations You Will Use to Manage Load and Asynchronous Services.

Streaming data refers to data that is continuously generated, usually in high volumes and at high speeds. A data source would typically consist of a stream of logs that record events as they happen.

Some examples of how I would manage data streaming applications are

1. Query Optimization
This is when a developer, or the database engine, changes a query in such a way that SQL Server is able to return the same results more efficiently.
Sometimes it's a simple as using EXISTS() instead of COUNT(), but other times the query needs to be rewritten with a different approach.
The goal of query optimization is to reduce the system resources required to fulfill a query

2. Formulation of continuous queries
Background data is continuously retrieved from the sources. But as soon as the
background data increase the volume and become distributed over the
Web, the time and cost to retrieve them increases, and consequently applications
are at risk of becoming unresponsive.
Continuous queries is proven to enhance the performance of the query processor.

3. Query transformation
Query transformation used by the optimizer to rewrite a query and optimizer it better.
You can pass parameters to the query to output multiple rows when the query has a select statement.

## Give examples of different encryption/hashing methods you have come across
## (one way and two way) and give example scripts in python 3 on how to achieve
## each one.

Hashing is probably the first way people are introduced to a programming language but you only get to know after you become well vast in a programming language.
Hashing is simply passing some data through a formula that produces a result. That hash is usually a string of characters and the hashes generated by a formula are always the same length. Examples of projects ive done that have the hashing concept incorporated include.

**[https://github.com/zecollokaris/Kenyanese-Problem](https://github.com/zecollokaris/Kenyanese-Problem)** 

**[https://github.com/zecollokaris/Password-Locker](https://github.com/zecollokaris/Password-Locker)** 

1. Collision Hashing
A collision or clash is a situation that occurs when two distinct pieces of data have the same hash value. In such a situation two or more data elements would qualify to be stored/mapped to the same location in the hash table

#### `Example`

```
A : B = L
A = B1 = L+1
```

2. Secure Hashing
An important application of secure hashes is the verification of message integrity.
Secure Hash Algorithms, also known as SHA, are a family of cryptographic functions designed to keep data secured.

#### `Example`

```
collins   collins123  ## HASH     ##  xxxxxxx
sam       sam123      ## FUNCTION ##  xxxxxxx
```

3. Inbuild Hashing
Python comes with an inbuid hashing function. On your terminal you can try this.

#### `Example`

```
$ python
>>> hash
<built-in function hash>
>>> hash("test")
2314058222102390712
```
4. Perceptual Hashing
Perceptual hashing is the name for a class of algorithms that attempts to produce a fingerprint of image data and other multimedia.
Perceptual hash functions are widely used to find cases of wide online copyright infringment.
For example when a user uploads a video that has a copyright on Youtube the hashes will be almost exactly the same and the video could be flagged as plagiarism.
