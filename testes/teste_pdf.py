# extracao do pdf 
from pathlib import Path
from src.conversor.pdf import extrair_texto_pdf
from src.conversor.audio import texto_para_audio

# local do pdf 
arquivo_pdf = Path("entrada/teste.pdf")


# verifica se o pdf existe 

if not arquivo_pdf.exists():

    print ("PDF nao encontrado", arquivo_pdf)
    raise SystemExit


# extrai o texto 
print("Extaindo texto do pdf")
texto= extrair_texto_pdf(arquivo_pdf)


# salva texto extraido 
arquivo_txt = Path("saida/teste_pdf.txt")

arquivo_txt.write_text(
    texto,
    encoding="utf-8",
)

# transforma pdf em audio 
arquivo_audio = Path("saida/teste_pdf.wav")

texto_para_audio(
    texto,
    arquivo_audio,
)

print(f"Áudio gerado: {arquivo_audio}")

# resultado 

print ("teste concluido")

print(f"PDF utilizado: {arquivo_pdf}")
print(f"TXT gerado: {arquivo_txt}")
print(f"Áudio gerado: {arquivo_audio}")
print(f"Quantidade de caracteres: {len(texto)}")g