# flask-opencv-study

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
