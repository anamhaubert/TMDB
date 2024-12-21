# python3 -m venv env

# ./env/scripts/activate

# pip install requests

# pip install "fastapi[standard]" uvicorn

# uvicorn main:app  

# fastapi dev main.py

pip freeze > requirements.txt

pip install python-dotenv

# Credenciais
Credenciais devem ser armazenadas em um arquivo de configuração,
que não está rastreado pelo controle de versão ou seja compartilhado.

## Instalar biblioteca dotenv
Permite a leitura do arquivo .env de configuração

```bash
pip install python-dotenv
```

## Importar token do ambiente 

```python
import os
import dotenv
dotenv.load_dotenv(".env")
token = os.environ["API_TOKEN"]
```

## Formato de URLs

### Query parameter
https://api.themoviedb.org/3/search/person?id=2000

### Url parameter 
https://api.themoviedb.org/3/search/person/2000

----

# API TMDB
- Cadastro no site para gerar a chave da API:
- https://www.themoviedb.org/settings/api

## Documentação
- https://developer.themoviedb.org/reference/intro/getting-started

# Criação do ambiente virtual Python
## cria a pasta env (somente uma vez)
```bash
python3 -m venv env
```

## Ativar o ambiente
Ativa o ambiente para usar no projeto.

```bash
source env/bin/activate

# windows
.\env\scripts\activate
```

### verifica qual o python esta sendo usado no terminal
```
which python
```

## Instalar biblioteca requests
```bash
pip install requests
```

# Servidor Web (FastAPI)

Instalar o fastapi e o servidor uvicorn

```bash
pip install "fastapi[standard]" uvicorn
```

## Inicia o servidor 
```bash
uvicorn main:app --reload
uvicorn main:app --reload --port=5000 # opcional se a port 8000 estiver em uso
```

## Verificar todos os endpoints
- http://127.0.0.1:8000/docs


---
---


# Desenvolvimento Web IV
- https://github.com/fscheidt/web4
- https://ava.ifpr.edu.br/course/view.php?id=12869


## Sobre a disciplina
- JSON (serialização de dados)
- API (application program interface)
- REST 

## Ambiente de desenvolvimento

Testar no terminal:

```bash
python3 --version
pip -V
```

extensão do vscode:
- thunder client



## JSON (formato)

Notação para representar dados, usando chave-valor

```json

{
  "id": 13491,
  "disciplina": "DESENVOLVIMENTO WEB IV",
  "curso": {
    "nome": "tads",
    "turma": 2023
  },
  "professores": ["Felippe"],
  "alunos": 14,
  "turno": "noturno",
  "ativa": true,
  "ava": null,
  "percentual": 5.5
}

```

Validação do json: 
- https://jsonlint.com/


## Atividade 1

Estruturar numa representação json informações sobre filmes e series

- https://filmow.com/pearl-t343849/ficha-tecnica/

Proponha um JSON que represente os dados contidos na página "ficha técnica".


## Atividade 2

Estruturar JSON para representar dados sobre a capital até Internet TLD do país Chile. Ver dados na página:
- https://en.wikipedia.org/wiki/Chile

python -m pip install "pymongo[srv]"

mongodb+srv://anamanskeana:Zd6f4lAVcMQaFmuZ@cluster0.dqrfj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

Zd6f4lAVcMQaFmuZ



