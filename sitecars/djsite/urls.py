from django.urls import path, re_path, include
from .views import *
urlpatterns = [
    path("", getData),
    path("add/", createData),
    path("update/", editData),
    path("search/", searchData),
    path("load/", loadData),
    path("getchar/", getCharacter),
    path('characters/', CharacterListView.as_view(), name='character-list'),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
