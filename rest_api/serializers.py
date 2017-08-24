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
# bucketlists = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Bucketlist.objects.all())


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""
    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username')

class FotoSerializer(serializers.ModelSerializer):
    produto_id = serializers.RelatedField(source='produto.id', read_only=True);
    class Meta:
        model = Foto
        fields = ('id', 'path','name', 'pub_date', 'produto_id')

class ProdutoSerializer(serializers.ModelSerializer):
    
    fotos = FotoSerializer(many=True)

    class Meta:
        model = Produto
        fields = ('id', 'first_name', 'last_name', 'thumb', 'email', 'fotos')



# class OwnerSerializer(serializers.ModelSerializer):  
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()

#     class Meta:
#         model = Owner
#         fields = ('first_name', 'last_name',)


# class BakerySerializer(serializers.Serializer):  
#     name = serializers.CharField()
#     owners = OwnerSerializer(many=True)  # This.

#     class Meta:
#         model = Bakery
#         fields = ('name', 'owners',)