from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


from .models import *
from .serializers import *

# class 

# GOOGLE

@api_view(['GET', 'POST'])
def google_list(request):
    if request.method == 'GET':
        snippets = Google.objects.all()
        serializer = GoogleSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GoogleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def google_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        googlenews = Google.objects.get(pk=pk)
    except Google.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GoogleSerializer(googlenews)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GoogleSerializer(googlenews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        googlenews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# APPLE

@api_view(['GET', 'POST'])
def apple_list(request):
    if request.method == 'GET':
        snippets = Apple.objects.all()
        serializer = AppleSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def apple_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        applenews = Apple.objects.get(pk=pk)
    except Apple.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppleSerializer(applenews)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppleSerializer(applenews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        applenews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# META
@api_view(['GET', 'POST'])
def meta_list(request):
    if request.method == 'GET':
        snippets = Meta.objects.all()
        serializer = MetaSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def meta_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        metanews = Meta.objects.get(pk=pk)
    except Meta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MetaSerializer(metanews)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MetaSerializer(metanews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        metanews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# MICROSOFT
@api_view(['GET', 'POST'])
def microsoft_list(request):
    if request.method == 'GET':
        snippets = Microsoft.objects.all()
        serializer = MicrosoftSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MicrosoftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def microsoft_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        microsoftnews = Microsoft.objects.get(pk=pk)
    except Microsoft.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MicrosoftSerializer(microsoftnews)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MicrosoftSerializer(microsoftnews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        microsoftnews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
