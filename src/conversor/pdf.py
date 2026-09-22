# leitura do pdf 
from pathlib import Path 
import pymupdf


# funcao pra extrair texto do pdf 

def extrair_texto_pdf(caminho_pdf):
    caminho_pdf = Path(caminho_pdf)
    documento = pymupdf.open(caminho_pdf)

    textos = []
    for pagina in documento:
        texto = pagina.get_text()
        textos.append(texto)

    documento.close()


    texto_completo = "\n\n".join(textos)

    return texto_completo