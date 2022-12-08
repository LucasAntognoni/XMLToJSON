from rest_framework import serializers
from rest_framework.fields import FileField
from django.core.validators import FileExtensionValidator


class ConvertSerializer(serializers.Serializer):

    file = FileField(validators=[FileExtensionValidator(['xml'])])
