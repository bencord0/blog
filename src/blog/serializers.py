from rest_framework import serializers


class SummaryEntrySerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    date = serializers.DateTimeField()
    summary = serializers.CharField()
