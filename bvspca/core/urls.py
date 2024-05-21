# -*- coding: utf-8 -*-
from bvspca.core import views
from django.urls import re_path

app_name = 'core'
urlpatterns = [
    re_path(
        r'^search/$',
        view=views.site_search,
        name='search'
    ),
]
