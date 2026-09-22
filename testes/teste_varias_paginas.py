from pathlib import Path
from time import perf_counter

from PIL import Image

from src.conversor.ocr import fazer_ocr
from src.conversor.audio import texto_para_audio

inicio_programa = perf_counter()

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

inicio_ocr = perf_counter()

for imagem_path in imagens:

    inicio_pagina = perf_counter()

    print(f"\nProcessando: {imagem_path.name}")

    imagem = Image.open(imagem_path)

    texto = fazer_ocr(
        imagem,
        idioma="por",
    )

    textos.append(texto)

    fim_pagina = perf_counter()

    tempo_pagina = fim_pagina - inicio_pagina

    print(f"Tempo desta página: {tempo_pagina:.2f} segundos")


fim_ocr = perf_counter()

tempo_total_ocr = fim_ocr - inicio_ocr

print(f"\nTempo total do OCR: {tempo_total_ocr:.2f} segundos")

# juntaa os textos 


texto_completo = "\n\n".join(textos)

# salva os textos da ocr 
arquivo_txt = Path("saida/texto_completo.txt")

inicio_txt = perf_counter()

arquivo_txt.write_text(
    texto_completo,
    encoding="utf-8",
)

fim_txt = perf_counter()

tempo_txt = fim_txt - inicio_txt

print(f"Tempo para salvar o TXT: {tempo_txt:.2f} segundos")

# transforma o texto completo em um audio 
arquivo_audio = Path("saida/livro_completo.wav")

inicio_audio = perf_counter()

texto_para_audio(
    texto_completo,
    arquivo_audio,
)

fim_audio = perf_counter()

tempo_total_audio = fim_audio - inicio_audio

print(
    f"Tempo para gerar o áudio: "
    f"{tempo_total_audio:.2f} segundos"
)

print("processo concluido")

print(f"Texto: {arquivo_txt}")
print(f"Áudio: {arquivo_audio}")



fim_programa = perf_counter()

tempo_total_programa = fim_programa - inicio_programa

print(
    f"Tempo total do programa: "
    f"{tempo_total_programa:.2f} segundos"
)