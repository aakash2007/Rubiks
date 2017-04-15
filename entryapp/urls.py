from django.urls import reverse_lazy
from django.conf.urls import url
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
	url(r'^$', RedirectView.as_view(url=reverse_lazy('entryapp:counter'))),
    url(r'^counter/$', counter, name='counter'),
    url(r'^app/$', app, name='app'),
]
