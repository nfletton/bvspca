from django.conf.urls import url

from bvspca.feeds.feeds import EventFeed, AllContentFeed, LatestNewsFeed, AnimalsFeed

urlpatterns = [
    url(r'^animals/$', AnimalsFeed()),
    url(r'^events/$', EventFeed()),
    url(r'^news/$', LatestNewsFeed()),
    url(r'^all/$', AllContentFeed()),
]
