from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(
        regex=r'^(?P<content_type>[-\w]+)/(?P<obj_id>\d+)/add/$',
        view='watchlist.views.watch',
        name="add_to_watchlist"
    ),
    url(
        regex=r'^(?P<content_type>[-\w]+)/(?P<obj_id>\d+)/remove/$',
        view='watchlist.views.unwatch',
        name="remove_from_watchlist"
    ),
    url(
        regex=r'^(?P<slug>[-\w]+)/$',
        view='watchlist.views.watchlist',
        name="user_watchlist"
    ),
    url(
        name="watchlist",
        regex=r'^$',
        view='watchlist.views.watchlist'
    ),
)
