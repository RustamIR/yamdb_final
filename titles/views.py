from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categories, Genres, Titles
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitleCreateSerializer, TitleListSerializer)
from api.permissions import ReadOnly, TitleAdmin
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .filters import TitlesFilter
from django.db.models import Count


class CustomListViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoriesViewSet(CustomListViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (ReadOnly | TitleAdmin,)
    filter_backends = [SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'


class GenresViewSet(CustomListViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (ReadOnly | TitleAdmin,)
    filter_backends = [SearchFilter]
    search_fields = ['name', ]
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    queryset = Titles.objects.all().annotate(Count('rating'))
    permission_classes = (ReadOnly | TitleAdmin,)
    filter_backends = [DjangoFilterBackend]
    filter_class = TitlesFilter

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitleCreateSerializer
        return TitleListSerializer
