from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer

@api_view(['POST'])
def create_file(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_files(request):
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_file_by_id(request, file_id):
    try:
        file_path = File.objects.get(id=file_id)
    except File.DoesNotExist:
        return Response({'message': 'File not found'}, status=404)

    serializer = FileSerializer(file_path)
    return Response(serializer.data)

@api_view(['PUT'])
def update_file(request, file_id):
    try:
        file_path = File.objects.get(id=file_id)
    except File.DoesNotExist:
        return Response({'message': 'File not found'}, status=404)

    serializer = FileSerializer(file_path, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_file(request, file_id):
    try:
        file_path = File.objects.get(id=file_id)
    except File.DoesNotExist:
        return Response({'message': 'File not found'}, status=404)

    file_path.delete()
    return Response({'message': 'File deleted'}, status=204)


@api_view(['DELETE'])
def delete_all_files(request):
    files = File.objects.all()
    files.delete()
    return Response({'message': 'All files deleted'}, status=204)