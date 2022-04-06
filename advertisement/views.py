from django.shortcuts import render

# Create your views here.
#TODO: CRUD объявления
#TODO: проверка прав: редактироватит и удалять объявление мог только автор
#TODO: категории может создавать, удалять, редактировать только админ
#TODO: фильтрация, поиск, пагинация
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from advertisement.models import Advertisement
from advertisement.serializers import CreateAdSerializer, AdvertisementListSerializer


class CreateAdvertisementView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = CreateAdSerializer
    permission_classes = [IsAuthenticated]


class AdvertisementsListView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer


class AdvertisementDetailsView(RetrieveAPIView):
    pass


class UpdateAdvertisementView(UpdateAPIView):
    pass


class DeleteAdvertisementView(DestroyAPIView):
    queryset = Advertisement.objects.all()
