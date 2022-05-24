from rest_framework import serializers
from myapp.models import *


class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBase
        fields = "__all__"