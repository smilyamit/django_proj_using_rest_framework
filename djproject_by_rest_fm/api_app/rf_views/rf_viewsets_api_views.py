from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from api_app.serializers import BlogSerializer
from api_app.models import BlogModel


class BlogViewSets(viewsets.ViewSet):
    def list(self, request):
        queryset = BlogModel.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    # Return one blog item
    def retrieve(self, request, pk=None):
        queryset = BlogModel.objects.all()
        if pk is not None:
            blog = get_object_or_404(queryset, pk=pk)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)


class BlogModelViewSets(viewsets.ModelViewSet):  # we have ModelViewSet, GenericViewSet, ReadonlyModelViewSet
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

    # def create(self, request, *args, **kwargs):
    #     if request.data.get('title') != '':
    #         serializer = BlogSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
