from pathlib import Path

from PIL import Image

from src.conversor.ocr import fazer_ocr
from src.conversor.audio import texto_para_audio


# localiza imagens 
pasta_entrada = Path("entrada")

# modelos de imagem 

imagens = sorted(
    [
        arquivo
        for arquivo in pasta_entrada.iterdir()
        if arquivo.suffix.lower() in [".jpg", ".jpeg", ".png"]
    ]
)

# verificar se tem imagens 
if not imagens:
    print("nenhuma imagem encontrada na pasta ")
    raise SystemExit

print(f"{len(imagens)}) imagem(ns) encontrada(s).")


# faz a ocr com todas as paginas 

textos = []

for imagem_path in imagens:
    print(f"\nProcessando:{imagem_path.name}")
    imagem = Image.open(imagem_path)

    texto = fazer_ocr(
        imagem,
        idioma = "por",
    )

    textos.append(texto)

# juntaa os textos 


texto_completo = "\n\n".join(textos)

# salva os textos da ocr 
arquivo_txt = Path("saida/texto_completo.txt")

arquivo_txt.write_text(
    texto_completo,
    encoding="utf-8",
)

# transforma o texto completo em um audio 
arquivo_audio = Path("saida/livro_completo.wav")

texto_para_audio(
    texto_completo,
    arquivo_audio,
)

print("processo concluido")

print(f"Texto: {arquivo_txt}")
print(f"Áudio: {arquivo_audio}")