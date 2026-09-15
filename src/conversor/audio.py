# importando as lib necessarias (modulo de audio) 
import pyttsx3


# Funcao Cria o mecanismo de conversao de txt para fala 
def criar_motor():
    return pyttsx3.init()


#Funcao Lista das vozes disponiveis 

def listas_vozes():
    motor = criar_motor()
    return motor.getProperty("voices")

# funcao transforma txt em audio 

def texto_para_audio(texto, caminho_saida):

    motor = criar_motor()
    motor.save_to_file(
        texto,
        str(caminho_saida),
    )

    motor.runAndWait()