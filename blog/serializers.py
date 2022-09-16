from django.db.models import fields
from rest_framework import serializers
from .models import Blog


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'image', 'date')


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title',)


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'image', 'date')
