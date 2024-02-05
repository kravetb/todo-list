from django.urls import path, include

urlpatterns = [
    path("", include("todo.urls", namespace="todo"))
]

app_name = "todo"
