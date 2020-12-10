from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Note
from .serializers import NoteSerializer
    
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def getAllNotes(request):
        if request.user.is_authenticated:
            user = request.user.id
            print(user)
        notes = Note.objects.filter(user_id=user).order_by('-id')
        print(notes)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    print(request.data)
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('saved sucessfully')
    return Response(serializer.data)


@api_view(['POST'])
def updateNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return JsonResponse(f"Deleted note ${pk}")