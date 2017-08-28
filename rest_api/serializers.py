from rest_framework import serializers
from .models import Produto, Foto
from django.contrib.auth.models import User

class FotoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Foto
        fields = ('id', 'path','name', 'pub_date')

class ProdutoSerializer(serializers.ModelSerializer):    
    fotos = FotoSerializer(many=True, read_only=True)

    class Meta:
        model = Produto
        fields = ('id', 'first_name', 'last_name', 'thumb', 'email', 'fotos')

    def create(self, validated_data):
        fotos_data = validated_data.pop('fotos')
        produto = Produto.objects.create(**validated_data)
        for foto_data in fotos_data:
            foto_data['produto'] = produto
            Foto.objects.create(produto=produto, **foto_data)
        return produto


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""
    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username')

# class OrderSerializer(serializers.ModelSerializer):
#    orderdetail_set = OrderDetailSerializer(many=true)
# POST

# def create(self, validated_data):
#     order_details_data = validated_data.pop('orderdetail_set')
#     order = Order.objects.create(**validated_data)

#     for order_detail_data in order_details_data:
#         order_detail_data['order'] = order
#         OrderDetail.objects.create(**order_detail_data)
#     return order 