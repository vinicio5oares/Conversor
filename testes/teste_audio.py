from pathlib import Path

from PIL import Image

from src.conversor.ocr import fazer_ocr
from src.conversor.audio import texto_para_audio



# 1. LOCALIZAR A IMAGEM


imagem_path = Path("entrada/Teste2.jpeg")



#  ABRIR A IMAGEM


imagem = Image.open(imagem_path)



#  FAZER O OCR


texto = fazer_ocr(imagem, idioma="por")



#  MOSTRAR O TEXTO RECONHECIDO


print("===== TEXTO RECONHECIDO PELO OCR =====")
print(texto)



#  DEFINIR O ARQUIVO DE ÁUDIO


saida = Path("saida/teste_audio.wav")



#  TRANSFORMAR O TEXTO DO OCR EM ÁUDIO


texto_para_audio(texto, saida)



# INFORMAR O RESULTADO


print("\n===== ÁUDIO =====")
print("Áudio criado com sucesso!")
print(f"Arquivo: {saida}")