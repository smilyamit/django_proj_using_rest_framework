from api_app.models import BlogModel
from api_app.serializers import BlogSerializer
from rest_framework import generics

class BlogPostListCreateApiView(generics.ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


