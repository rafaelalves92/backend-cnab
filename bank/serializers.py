from rest_framework import serializers

from .models import Bank


class BankSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tipo = serializers.IntegerField()
    data = serializers.DateField()
    valor = serializers.IntegerField()
    cpf = serializers.CharField()
    cartao = serializers.CharField()
    hora = serializers.TimeField()
    dono_loja = serializers.CharField()
    nome_loja = serializers.CharField()

    def create(self, validated_data):
        cnab_obj = Bank.objects.create(**validated_data)

        return cnab_obj
