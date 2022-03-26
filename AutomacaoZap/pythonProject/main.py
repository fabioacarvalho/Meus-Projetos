# Importar Libs:

import pywhatkit
import keyboard
import time
from datetime import datetime
import pandas as pd

# Importando Contatos:

contatos = pd.read_excel("teste.xlsx")

arr = []

# Intervalo de envio:

for i, telefone in enumerate(contatos['telefone']):
    numero = '+' + str(contatos.loc[i, "telefone"])
    arr.append(numero)


def enviar():
    while len(arr) >= 1:
        # pywhatkit.sendwhatmsg(arr[0], 'Teste Bot Whatsapp', datetime.now().hour, datetime.now().minute + 1)
        pywhatkit.sendwhats_image(arr[0], "Images/fly.png", "Oi confira as novidades...")
        del arr[0]
        time.sleep(3)
        keyboard.press_and_release('ctrl + w')


