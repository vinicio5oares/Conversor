# Importaçoes
from pathlib import Path

import pytesseract
from PIL import Image

# Localização do tesseract 
TESSERACT_PATH = Path(
     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Informa ao tesseract o caminho a ser seguido na execuçao ja que ele nao esta no PATH do windows 
pytesseract.pytesseract.tesseract_cmd = str (TESSERACT_PATH)


# Funcao para verificar o tesseract 
def verificar_tesseract():
    return str(pytesseract.get_tesseract_version())
# Funcao para ver a lista de idiomas instalados 

def listar_idiomas():
    return pytesseract.get_languages(config="")

# Funcao para fazer a ocr 
def fazer_ocr(imagem: Image.Image, idioma="por"):
    return pytesseract.image_to_string(
        imagem,
        lang=idioma,
    )