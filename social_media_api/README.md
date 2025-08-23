# Social Media API — Auth

## Setup
pip install django djangorestframework pillow
pip install djangorestframework-authtoken

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Apps
- accounts (custom user + auth)

## Settings
- AUTH_USER_MODEL=accounts.User
- TokenAuthentication enabled via DRF and rest_framework.authtoken

## Endpoints
- POST /register → returns { token, user }
- POST /login    → returns { token, user }
- GET/PUT/PATCH /profile (Token auth)

## User model
Extends AbstractUser with:
- bio (TextField)
- profile_picture (ImageField)
- followers (ManyToMany to self, symmetrical=False, related_name='following')
