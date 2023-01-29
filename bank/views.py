from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import Request

from .serializers import BankSerializer


def fileForm(request: Request):
    if request.method == "GET":
        return render(request, "form.html")
    elif request.method == "POST":
        cnab_bytes = request.FILES["file"].read()
        cnab_txt = cnab_bytes.decode("UTF-8")
        cnab_array = cnab_txt.split("\n")

        for item in cnab_array:
            obj = {
                "tipo": item[0],
                "data": f"{item[1:5]}-{item[5:7]}-{item[7:9]}",
                "valor": int(item[9:19]),
                "cpf": item[19:30],
                "cartao": item[30:42],
                "hora": f"{item[42:44]}:{item[44:46]}:{item[46:48]}",
                "dono_loja": item[48:62],
                "nome_loja": item[62:80],
            }

            serializer = BankSerializer(data=obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return HttpResponse("Arquivo enviado com sucesso!")
