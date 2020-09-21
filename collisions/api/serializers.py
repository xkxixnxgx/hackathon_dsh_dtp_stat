from rest_framework import serializers
from ..models import Collision  # необходимо описать модель


class CollisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collision
