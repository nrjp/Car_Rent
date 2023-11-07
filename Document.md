# Django before Production


### Rest Api Authentications


### CORS


### Generate SECRET_KEY

- python3 manage.py shell    
- from django.core.management.utils import get_random_secret_key
- print(get_random_secret_key())

### Add Domanin Name 

- ALLOWED_HOSTS

### Add STATIC_ROOT

- STATIC_URL = '/static/'
- STATIC_URL

### Hide sensitive information in .env

1. SECRET_KEY
2. DEBUG = False
3. Email config
4. Database config
5. ALLOWED_HOSTS

### HTTP Setting

- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- SECURE_SSL_REDIRECT = True

### HSTS Setting

- SECURE_HSTS_SECONDS =       # 1 year
- SECURE_HSTS_PRELOAD = True
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True

### Run Check

- python manage.py check --deploy
