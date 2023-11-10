# flask-opencv-study

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.0.x/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

Estudos aleatórios para relembrar como funciona o Flask e o OpenCV.

Projetinho absolutamente simples, um botão de upload de imagem, o flask recebe
essa imagem, a converte para escalas de cinza usando openCV, e fornece um link
para download da imagem convertida.

## Desenvolvimento

### Pré requisitos:

- Docker
- Docker compose

### Subindo o ambiente

```sh
docker-compose up
```

- Acesse: http://127.0.0.1:5000/

## Formatação automática com black

```sh
black --line-length 79
```
