import os

from blog import views

STATIC_PREFIX = os.getenv('STATIC_PREFIX', 'http://localhost:8000/static/')
PORT = os.getenv('PORT', 8000)
URLMAP = (
    (b'/', views.IndexView()),
)
