import django_heroku


DEBUG = False

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 1

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

ALLOWED_HOSTS = ['acmf-dev.herokuapp.com']

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

django_heroku.settings(locals())