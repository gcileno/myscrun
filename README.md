# Uma solução gratuita para gerencimaneto de projetos no modelo ScrunMaster

# Ambiente de desenvolvimento

## Crie um arquivo .env
No arquivo criado, insira suas credenciasi de banco de dados postgreSql
A secret key da sua aplicação
demais variaveis sensiveis conforme o arquivo .env.example

## Requisitos de instalação
```
python => 3.13
poetry
```
## Dependencias
Estão listadas no arquivo pyproject.toml

## Iniciar projeto
execute o comando:

```
poetry install
```
ele deverá instalar todas as dependencias do sistema sem muito esforço por parte do programador

## Tabelas

```
poetry run manage.py makemigrations
poetry run manage.py migrate
```
## Criar super-user
```
poetry run manage.py createsuperuser
```
## Execute o programa levantando o servidor
```
poetry run manage.py runserver
```