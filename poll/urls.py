from django.urls import path

from . import views

app_name = "poll"

urlpatterns = [

    path("", views.IndexView.as_view(), name="index"),
    path("add/", views.CreateView.as_view(), name="poll_add"),
    path("<int:pk>/edit/", views.PollUpdateView.as_view(), name="poll_edit"),
    path("<int:pk>/delete/", views.PollDeleteView.as_view(), name="poll_delete"),
    path("<int:pk>/", views.DetailView.as_view(), name="poll_details"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]