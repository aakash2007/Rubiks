from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from views import RegisterView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
]
