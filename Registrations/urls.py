from django.conf.urls import url
from django.contrib import admin

from views import RegisterView

urlpatterns = [
    url(r'^$', RegisterView.as_view()),
]
