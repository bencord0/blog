import os

from blog import views

PORT = os.getenv('PORT', 8000)
URLMAP = (
    (b'/', views.IndexView()),
    (b'/defer', views.DeferView()),
    (b'/async', views.AsyncView()),
    (b'/counter', views.CounterView()),
)
