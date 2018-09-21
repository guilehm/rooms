# Rooms - Gestão de Salas de Reunião
[![Build Status](https://travis-ci.com/Guilehm/rooms.svg?branch=master)](https://travis-ci.com/Guilehm/rooms)

**Gerencie suas salas e eventos com este sistema.**

---
# Exemplo em produção para testes
https://gui-rooms.herokuapp.com/


# Visão Geral

* Interface para criação, visualização e edição de salas de reunião.
* Interface para criação, visualização e edição de reuniões.
* [Calendário](https://gui-rooms.herokuapp.com/meeting/calendar/) de visualização das reuniões com visão mensal, semanal e diária.
* API - CRUD com Django Rest Framework utilizando Serializers e Class Based Views.
* Documentações da API: [Swagger](https://gui-rooms.herokuapp.com/swagger/), [Redoc](https://gui-rooms.herokuapp.com/redoc/), [DRF Docs](https://gui-rooms.herokuapp.com/docs/).
* Testes automatizados utilizando Pytest.
* Construção do projeto documentada utilizando Git com criação de Issues e Pull Requests.
* Integração contínua com Travis-CI.
* Gerar logs de qualquer Exception e de qualquer interação com a API.
* Utilização do Isort, Flake8, Django Debug Toolbar e Django Extensions.
* Deploy no Heroku com PostgreSQL. 
* Logentries para gerenciamento de logs.

# Requisitos

* Python (3.6)
* Django (2.1)

# Instalação

Clone este repositório

    git clone https://github.com/Guilehm/rooms.git

Entre no diretório

    cd rooms
    
Instale o pipenv

    pip install pipenv
    
Crie o ambiente virtual e instale as dependências

    pipenv install
    
Ative o ambiente virtual 

    pipenv shell

Aplique as migrations

    python manage.py migrate

Inicie o servidor

    python manage.py runserver

Agora o projeto está rodando em [http://localhost:8000/](http://localhost:8000/).

# Utilização

**Crie uma sala:**
- Interface web em [http://localhost:8000/room/add/](http://localhost:8000/room/add/). Ou
- POST Create em [http://localhost:8000/api/rooms/](http://localhost:8000/api/rooms/) com o seguinte payload:
```json
{
    "name": "São Paulo",
    "slug": "sao-paulo",
    "description": "Sala com televisão para até 5 pessoas.",
    "color": "green"
}
```

**Crie uma reunião:**
- Interface web em [http://localhost:8000/meeting/add/](http://localhost:8000/meeting/add/). Ou
- POST Create em [http://localhost:8000/api/meetings/](http://localhost:8000/api/meetings/) com o seguinte payload:
```json
{
    "name": "Apresentação do projeto",
    "room": 1,
    "description": "Apresentação do projeto para o cliente.",
    "status": "scheduled",
    "date": "22/09/2018",
    "start": "08:00",
    "end": "11:30"
}
```

**Visualize sua reunião:**
- Calendário em [http://localhost:8000/meeting/calendar/](http://localhost:8000/meeting/calendar/). Ou
- Interface web em [http://localhost:8000/meeting/list/](http://localhost:8000/meeting/list/). Ou
- GET em [http://localhost:8000/api/meetings/](http://localhost:8000/api/meetings/) 

**Gerencie, pesquise e filtre suas reuniões:**
- Interface web em [http://localhost:8000/meeting/calendar/](http://localhost:8000/meeting/calendar/). Ou
- GET em [http://localhost:8000/api/meetings/](http://localhost:8000/api/meetings/):

**Filtros: (podem ser combinados)**
- Filtro por sala: `?room=1`
- Filtro por data: `?date=2018-09-22`
- Filtro por status: `?status=canceled` ou `?status=scheduled`
- Por hora de início exata: `?start=08:00`
- Por hora de termino exata: `?end=11:30`
- Por hora de início maior que: `?start_gte=07:00`
- Por hora de termino menor que: `end_lte=15:00`

**Edite suas reuniões**
- Interface web em [http://localhost:8000/meeting/1/change/](http://localhost:8000/meeting/1/change/). Ou
- PUT em [http://localhost:8000/api/meetings/1/](http://localhost:8000/api/meetings/1/) com o seguinte payload:
```json
{
    "id": 1,
    "name": "Apresentação do projeto",
    "room": 1,
    "description": "Apresentação do projeto para o cliente.",
    "status": "scheduled",
    "date": "23/09/2018",
    "start": "14:00",
    "end": "16:30"
}
```
- DELETE em [http://localhost:8000/api/meetings/1/](http://localhost:8000/api/meetings/1/)

# Django Admin
Crie o superuser executando

    python manage.py createsuperuser
    
Digite o nome de usuário

    admin
    
Digite o email (opcional)

    usuario@gmail.com
    
Digite e confirme a senha.

Acesse a interface neste link [http://localhost:8000/admin/](http://localhost:8000/admin/)

# Testes

Verifique se os imports estão ordenados corretamente

    isort
    
Verifique se o código está em ordem

    flake8

Execute os testes

    pytest -vv
    
Ou rode todos de uma só vez

    make test
    
# Imagens

![screenshot from 2018-09-20 22-44-34](https://user-images.githubusercontent.com/33688752/45855562-16e0b700-bd27-11e8-9182-135164d78f46.png)

![screenshot from 2018-09-20 22-45-30](https://user-images.githubusercontent.com/33688752/45855574-24963c80-bd27-11e8-95ee-8fa2e9a7789a.png)


![screenshot from 2018-09-20 22-45-56](https://user-images.githubusercontent.com/33688752/45855579-3081fe80-bd27-11e8-9893-f71b1c80b479.png)


