from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note


@api_view(['GET'])
def getRouts(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def getNotes(request):

    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):

    data = request.data
    note = Note.objects.create(body=data["body"])
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_delete_Note(request, pk):

    if request.method == "GET":
        note = get_object_or_404(Note, id=pk)
        serializer = NoteSerializer(note)

        return Response(serializer.data)

    if request.method == "PUT":
        note = get_object_or_404(Note, id=pk)
        serializer = NoteSerializer(instance=note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    if request.method == "DELETE":
        note = get_object_or_404(Note, id=pk)
        note.delete()

        return Response('Note was deleted')
