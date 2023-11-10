# flask-opencv-study

Estudos aleatórios para relembrar como funciona o Flask e o OpenCV.

Projetinho absolutamente simples, um botão de upload de imagem, o flask recebe
essa imagem, a converte para escalas de cinza usando openCV, e fornece um link
para download da imagem convertida.

## Iniciando

- Acesse a pasta `src/`

```sh
flask --app main run --host=0.0.0.0 --debug
```

## Formatação automática com black

```sh
black --line-length 79
```
