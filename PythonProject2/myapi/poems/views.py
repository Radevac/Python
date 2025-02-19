from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Poem, Author, Theme
from .serializers import PoemSerializer, AuthorSerializer, ThemeSerializer
import random
from rest_framework import status

@api_view(['GET'])
def get_random_poem(request):
    poems = Poem.objects.all()
    poem = random.choice(poems) if poems else None
    return Response(PoemSerializer(poem).data if poem else {"message": "No poems found."})

@api_view(['GET'])
def get_poem_by_author(request):
    author_name = request.GET.get('name')
    poems = Poem.objects.filter(author__name=author_name)
    poem = random.choice(poems) if poems else None
    return Response(PoemSerializer(poem).data if poem else {"message": "No poems for this author."})

@api_view(['GET'])
def get_poem_by_theme(request):
    theme_name = request.GET.get('name')
    poems = Poem.objects.filter(theme__name=theme_name)
    poem = random.choice(poems) if poems else None
    return Response(PoemSerializer(poem).data if poem else {"message": "No poems for this theme."})

@api_view(['GET'])
def get_all_authors(request):
    authors = Author.objects.all()
    return Response(AuthorSerializer(authors, many=True).data)

@api_view(['GET'])
def get_all_themes(request):
    themes = Theme.objects.all()
    return Response(ThemeSerializer(themes, many=True).data)

@api_view(['GET'])
def get_titles_by_author(request):
    author_name = request.GET.get('name')
    poems = Poem.objects.filter(author__name=author_name).values_list('title', flat=True)
    return Response({"titles": list(poems)})

@api_view(['GET'])
def get_titles_by_theme(request):
    theme_name = request.GET.get('name')
    poems = Poem.objects.filter(theme__name=theme_name).values_list('title', flat=True)
    return Response({"titles": list(poems)})

@api_view(['POST'])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_theme(request):
    serializer = ThemeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_poem(request):
    serializer = PoemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_poem(request, poem_id):
    try:
        poem = Poem.objects.get(id=poem_id)
    except Poem.DoesNotExist:
        return Response({"error": "Poem not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PoemSerializer(poem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_poem(request, poem_id):
    try:
        poem = Poem.objects.get(id=poem_id)
    except Poem.DoesNotExist:
        return Response({"error": "Poem not found"}, status=status.HTTP_404_NOT_FOUND)

    poem.delete()
    return Response({"message": "Poem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

