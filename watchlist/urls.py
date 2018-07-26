from django.urls import path

from . import views

urlpatterns =[
    path(
        '<slug:content_type>/<int:obj_id>/add/',
        views.watch,
        name="add_to_watchlist"
    ),
    path(
        '<slug:content_type>/<int:obj_id>/remove/',
        views.unwatch,
        name="remove_from_watchlist"
    ),
    path('<slug:slug>/', views.watchlist, name="user_watchlist"),
    path('', views.watchlist, name="watchlist"),
]
