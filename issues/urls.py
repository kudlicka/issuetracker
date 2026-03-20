from django.urls import path

from . import views

urlpatterns = [
    path("", views.list, name="list"),
    path("add/", views.add, name="add"),
    path("<int:issue_id>/", views.view, name="view"),
    path("<int:issue_id>/comment/", views.comment, name="comment"),
    path("<int:issue_id>/screenshot/", views.screenshot, name="screenshot"),
]
