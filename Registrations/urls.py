from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from views import RegisterView

urlpatterns = [
    url(r'^$', RegisterView.as_view(), name="register"),
    url(r'^wrs/$', TemplateView.as_view(template_name='index.html'), name="wrs"),
]
