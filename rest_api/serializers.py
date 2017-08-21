from rest_framework import serializers
from .models import Produto, Foto
from django.contrib.auth.models import User


# class BucketlistSerializer(serializers.ModelSerializer):
#     """Serializer to map the model instance into json format."""

#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         """Map this serializer to a model and their fields."""
#         model = Bucketlist
#         fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
#         read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    # bucketlists = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Bucketlist.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username')


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = ('id', 'path','name', 'pub_date')

class ProdutoSerializer(serializers.ModelSerializer):
    """
    fotos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Foto.objects.all())
    """
    fotos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Produto
        fields = ('id', 'first_name', 'last_name', 'thumb', 'email', 'fotos')


# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Album
#         fields = ('album_name', 'artist', 'tracks')
