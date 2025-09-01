import django_filters
from .models import RickAndMortyCharacter, Origin


class CharacterFilter(django_filters.FilterSet):
    # Простая фильтрация по точному совпадению
    name = django_filters.CharFilter(field_name='name', lookup_expr='exact')

    # Фильтрация с регистронезависимым поиском
    name_icontains = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )

    class Meta:
        model = RickAndMortyCharacter
        fields = ['name']