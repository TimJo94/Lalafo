import rest_framework.pagination
from django.shortcuts import render

# Create your views here.
#TODO: CRUD объявления
#TODO: проверка прав: редактироватит и удалять объявление мог только автор
#TODO: категории может создавать, удалять, редактировать только админ
#TODO: фильтрация, поиск, пагинация
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from advertisement.models import Advertisement, Category
from advertisement.permissions import IsAuthor
from advertisement.serializers import AdvertisementListSerializer, AdvertisementSerializer, CategorySerializer


# class CreateAdvertisementView(CreateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = CreateAdSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#
# class AdvertisementsListView(ListAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementListSerializer


# class AdvertisementDetailsView(RetrieveAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementDetailsSerializer

#
# class UpdateAdvertisementView(UpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = UpdateAdvertisementSerializer
#     permission_classes = [IsAuthor]


# class DeleteAdvertisementView(DestroyAPIView):
#     queryset = Advertisement.objects.all()
#     permission_classes = [IsAuthor]


# class AdPagination(rest_framework.pagination.PageNumberPagination):
#     page_size = 5
class AdvertisementFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Advertisement
        fields = ['category', 'city']


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['title', 'text', 'city']
    ordering_fields = ['price', 'title']
    filterset_class = AdvertisementFilter
    # pagination_class = AdPagination

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = AdvertisementListSerializer
        return serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        return []


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []

# ads/      create/list
# ads/id    details, update, destroy
