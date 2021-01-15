from abc import ABC

from rest_framework import permissions, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_json_api.django_filters import DjangoFilterBackend

from .serializer import RoomSerializer, BookingSerializer


class CreateViewMixin(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data = {
            'id': serializer.data['id']
        }
        return Response(data, status=status.HTTP_201_CREATED)


class InfoViewMixin(ListAPIView):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    @property
    def model(self):
        return self.serializer_class.Meta.model


class DeleteViewMixin(APIView):
    permission_classes = [permissions.AllowAny]

    def delete(self, request, pk):
        operand = get_object_or_404(self.model.objects.all(), pk=pk)
        operand.delete()
        return Response({'message': f'Object {pk} has been deleted'},
                        status=status.HTTP_204_NO_CONTENT)

    @property
    def model(self):
        return self.serializer_class.Meta.model


class RoomInfoView(InfoViewMixin):
    serializer_class = RoomSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['price', 'date_add']


class RoomCreateView(CreateViewMixin):
    serializer_class = RoomSerializer


class RoomDeleteView(DeleteViewMixin):
    serializer_class = RoomSerializer


class BookingInfoView(InfoViewMixin):
    serializer_class = BookingSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['date_start']
    filterset_fields = ['room']


class BookingCreateView(CreateViewMixin):
    serializer_class = BookingSerializer


class BookingDeleteView(DeleteViewMixin):
    serializer_class = BookingSerializer

