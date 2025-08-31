from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import requests
from django.db import transaction
# Create your views here.


@api_view(["GET"])
def getData(request):
    person = Item.objects.all()
    serializer = ItemSerializer(person, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(["POST"])
def createData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def editData(request):
    serializer = UpdateSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        person = Item.objects.get(id=serializer.data["id"])
        person.name = serializer.data["name"]
        person.save()

    return Response({"ok": "ok"})


@api_view(["POST"])
def searchData(request):
    serializer = SearchDataSerializer(data=request.data)
    if serializer.is_valid():
        person = Item.objects.filter(name=serializer.data["name"]).values()
        print(type(person))
        if person:
            return Response(person)
        return Response({"error": "User isn't found"})
    return Response({"error": "Data is not valid"})


@transaction.atomic
@api_view(["GET"])
def loadData(request):
    baseurl = "https://rickandmortyapi.com/api/"
    endpoint = "character"
    r = requests.get(baseurl + endpoint).json()
    pages = r["info"]["pages"]
    for page in range(pages):
        req = requests.get(baseurl + endpoint + f"/?page={page}").json()["results"]
        for character in req:
            try:
                origin = Origin.objects.create(
                    name=character["origin"]["name"],
                    url=character["origin"]["url"]
                )
                char = RickAndMortyCharacter.objects.create(
                        name=character["name"],
                        status=character["status"],
                        species=character["species"],
                        origin=origin,  # передаем объект Origin
                        created=character["created"]
                    )
            except Exception as e:
                print(f"Ошибка: {e}. Транзакция откачена!")
                raise  # Важно! Без raise транзакция НЕ откатится

    print(pages)
    print(r["results"][0])
    return Response({"response_code": r})


@api_view(["GET"])
def getCharacter(request):
    character = RickAndMortyCharacter.objects.select_related('origin').get(id=1)
    print(f"Character: {character.name}")
    print(f"From: {character.origin.name}")
    return Response({"ok": "ok"})



