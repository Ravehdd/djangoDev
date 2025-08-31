from django.urls import path
from .views import *
urlpatterns = [
    path("", getData),
    path("add/", createData),
    path("update/", editData),
    path("search/", searchData),
    path("load/", loadData),
    path("getchar/", getCharacter)
]
