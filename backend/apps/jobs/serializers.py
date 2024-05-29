from rest_framework import serializers

class JobSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    company = serializers.CharField(source='company.display_name')
    location = serializers.CharField(source='location.display_name')
    description = serializers.CharField()
    category = serializers.CharField(source='category.label')
    created = serializers.DateTimeField()