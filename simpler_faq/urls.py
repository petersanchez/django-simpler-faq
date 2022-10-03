#! coding: utf-8
from .views import Topics

try:
    from django.urls import path
    urlpatterns = [
        path('', Topics.as_view(), name='faq'),
    ]
except ImportError:
    from django.conf.urls import url
    urlpatterns = [
        url(r'^', Topics.as_view(), name='faq'),
    ]

