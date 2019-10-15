# Django Parse Request Body Middleware

## What is it

Before

```python
def view(request):
    # I want to use request body
    import json
    data = json.loads(request.body)
    ...
```

Now

```python
def view(request):
    # use request body directly
    request.data
```

## Compatibilities

* Python 3.5+
* Django 1.11+, 2.1+, 3.0 not sure

> Not sure work fine in other version.

### Request body type

* [x] form-data
* [x] application/json
* [ ] x-www-form-urlencoded
  * Test needed
* [ ] raw
  * Test needed
* [ ] binary
  * Test needed

## Usage

1. Put `middleware.py` and `util.py` to your django projects in same folder.
2. Add `RequsetBodyParseMiddleware` to your `settings.py`.

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "<path.to.your.folder>.middleware.RequsetBodyParseMiddleware",
]
```
