import pandas as pd

contato_df = pd.read_excel("teste.xlsx")

display(contato_df)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

#Enquanto não encontrar o elemento pane-side espere um 1 segundo.
while len(navegador.find_elements_by_id("pane-side")) < 1:
    time.sleep(1)
    
#Mandar as mensagens
for i, mensagem in enumerate(contato_df['mensagem']):
    pessoa = contato_df.loc[i, "nome"]
    numero = contato_df.loc[i, "telefone"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("pane-side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
