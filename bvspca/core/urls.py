# -*- coding: utf-8 -*-
from bvspca.core import views
from django.conf.urls import url

app_name = 'core'
urlpatterns = [
    url(
        regex=r'^search/$',
        view=views.site_search,
        name='search'
    ),
]
