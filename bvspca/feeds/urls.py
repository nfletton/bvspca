from django.urls import re_path

from bvspca.feeds.feeds import EventFeed, AllContentFeed, LatestNewsFeed, AnimalsFeed

urlpatterns = [
    re_path(r'^animals/$', AnimalsFeed()),
    re_path(r'^events/$', EventFeed()),
    re_path(r'^news/$', LatestNewsFeed()),
    re_path(r'^all/$', AllContentFeed()),
]
