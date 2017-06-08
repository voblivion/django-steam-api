# django-steam-api
Steam api models for django

## Installation

```
pip install django_steam_api
```

## Configuration

First install the app and set your Steam API key :
```
INSTALLED_APPS = (
    //...
    'django_steam_api',
    //...
)

STEAM_API_KEY = 'YOURSTEAMAPIKEY'
```

Then update database scheme  :
```
./manage.py migrate
```

## Usage

Import models and use custom objects methods to populate the databse.
Currently :
```
Player.objects.steam_create(id)
```
