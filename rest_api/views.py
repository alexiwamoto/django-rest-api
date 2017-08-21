from rest_framework import generics, permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .permissions import IsOwner
from .serializers import UserSerializer, ProdutoSerializer
from .models import Produto, Foto
from django.contrib.auth.models import User






# class CreateView(generics.ListCreateAPIView):
#     """This class handles the GET and POSt requests of our rest api."""
#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer
#     permission_classes = (
#         permissions.IsAuthenticated,
#         IsOwner)

#     def perform_create(self, serializer):
#         """Save the post data when creating a new bucketlist."""
#         serializer.save(owner=self.request.user)


# class DetailsView(generics.RetrieveUpdateDestroyAPIView):
#     """This class handles GET, PUT, PATCH and DELETE requests."""

#     queryset = Bucketlist.objects.all()
#     serializer_class = BucketlistSerializer
#     permission_classes = (
#         permissions.IsAuthenticated,
#         IsOwner)


# class UserView(generics.ListAPIView):
#     """View to list the user queryset."""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetailsView(generics.RetrieveAPIView):
#     """View to retrieve a user instance."""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class ProdutoList(APIView):
#     """
#     List all users, or create a new user.
#     """
#     def get(self, request, format=None):
#         produtos = Produto.objects.all()
#         serializer = ProdutoSerializer(produtos, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProdutoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         produto = self.get_object(pk)
#         produto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ProdutoDetail(APIView):
#     """
#     Retrieve, update or delete a user instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Produto.objects.get(pk=pk)
#         except Produto.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         produto = self.get_object(pk)
#         produto = ProdutoSerializer(produto)
#         return Response(produto.data)

#     def put(self, request, pk, format=None):
#         produto = self.get_object(pk)
#         serializer = ProdutoSerializer(produto, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         produto = self.get_object(pk)
#         produto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def produto_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def produto_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """

    try:
        produto = Produto.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
