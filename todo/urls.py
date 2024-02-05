from django.urls import path

from todo.views import HomePageView, TagListView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "todo"
