from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Blog
from .serializers import ItemSerializer

from rest_framework import serializers, permissions
from rest_framework import status


@api_view(['GET'])
def overview_blog(request):
    api_urls = {
        'all_items': '/all',
        # 'Search by Category': '/?category=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_blog(request):
    item = ItemSerializer(data=request.data)

    if Blog.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_blog(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Blog.objects.filter(**request.query_param.dict())
    else:
        items = Blog.objects.all()

    serializer = ItemSerializer(items, many=True)

    if items:
        # data = ItemSerializer(items)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_blog(request, pk):
    item = Blog.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_blog(request, pk):
    item = get_object_or_404(Blog, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


