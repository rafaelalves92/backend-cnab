# Documentação da API

## Tabela de Conteúdos

- [Visão Geral](#1-visão-geral)
- [Início Rápido](#2-início-rápido)   
    - [Migrations](#21-migrations)
- [Endpoints](#3-endpoints)

---

## 1. Visão Geral

Visão geral do projeto, um pouco das tecnologias usadas.

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [SQLite3](https://sqlite.org/)

---

## 2. Início Rápido
[ Voltar para o topo ](#tabela-de-conteúdos)

1- Clone o projeto em sua máquina.

2- Crie um ambiente virtual:

```shell
python -m venv venv
```

3- Ative o ambiente virtual:

```shell
.\venv\Scripts\activate
```

4- Instale todas as dependências:

```shell
pip install -r requirements.txt
```

### 2.1. Migrations

Execute as migrations com o comando:

```
python manage.py migrate
```
"Logo após o comando um arquivo db.sqlite3 será criado"

---

## 3. Utilizando o App

[ Voltar para o topo ](#tabela-de-conteúdos)

1- Rode o servidor:
```
python manage.py runserver
```

2- Acesse a rota localhost:8000/api/cnab/ pelo seu navegador.

3- Selecione um arquivo ".TXT" que contenha informações de transições bancárias no padrão CNAB e clique em "Enviar".

4- Após submeter o arquivo com sucesso, todas as informações estarão disponíveis no banco de dados no arquivo "db.sqlite3". 
