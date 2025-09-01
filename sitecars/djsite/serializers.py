from rest_framework import serializers
from .models import Item, Origin, RickAndMortyCharacter


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class UpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)


class SearchDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ['id', 'name', 'url']
        read_only_fields = ['id']


class RickAndMortyCharacterSerializer(serializers.ModelSerializer):
    # Вложенный сериализатор для чтения
    origin = OriginSerializer(read_only=True)

    # ID для записи (write-only)
    origin_id = serializers.PrimaryKeyRelatedField(
        queryset=Origin.objects.all(),
        source='origin',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = RickAndMortyCharacter
        fields = [
            'id',
            'name',
            'status',
            'species',
            'origin',  # для чтения (объект)
            'origin_id',  # для записи (ID)
            'created'
        ]
        read_only_fields = ['id', 'created']