from pathlib import Path

from PIL import Image

from src.conversor.ocr import fazer_ocr


# Caminho da imagem de teste
imagem_path = Path("entrada/teste1.jpeg")


# Abre a imagem
imagem = Image.open(imagem_path)


# Faz o OCR em português
texto = fazer_ocr(imagem, idioma="por")


# Mostra o resultado
print("TEXTO RECONHECIDO ")
print(texto)