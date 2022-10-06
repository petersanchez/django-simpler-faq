try:
    from django.urls import re_path
except ImportError:
    from django.conf.urls import url as re_path

from .views import Topics


urlpatterns = [
    re_path(r'^', Topics.as_view(), name='faq'),
]

