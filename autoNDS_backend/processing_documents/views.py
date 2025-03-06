from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer
from .utils import extract_pdf_data
import os


class DocumentListView(APIView):
    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents,  many=True)
        return Response(serializer.data)

    def post(self, request):
        print('0')
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "Файл не найден"}, status=status.HTTP_400_BAD_REQUEST)

        print('a')
        temp_file_path = f'temp_{file.name}'
        with open(temp_file_path, 'wb+') as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)

        print('b')
        pdf_data = extract_pdf_data(temp_file_path)
        os.remove(temp_file_path)  # Удаляем временный файл

        print('c')
        data = {
            'title': pdf_data['title'],
            'file': file,  # Файл из запроса
            'authors': pdf_data['authors'],
            'year': pdf_data['year'],
            'content': pdf_data['content'],
            'file_path': pdf_data['file_path'],  # Путь к файлу
        }
        print(data)
        serializer = DocumentSerializer(data=data)
        if serializer.is_valid():
            print('f')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print('e')
        print(serializer.errors)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        document = self.get_object(pk)
        if document:
            document.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)