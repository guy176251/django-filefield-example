from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from .models import SomeModel


class SomeSerializer(ModelSerializer):
    class Meta:
        model = SomeModel
        fields = "__all__"


class SomeViewSet(ModelViewSet):
    queryset = SomeModel.objects.all()
    serializer_class = SomeSerializer
