from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from DisparoWppDestinos import lista_envio


#VARIÁVEIS:
url = 'https://web.whatsapp.com/'
imagem_entrada = '//*[@id="app"]/div/div/div[3]/header/div[1]'
caixa_pesquisa_contatos = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
caixa_mensagem = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
clips_anexos = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
anexo_imagem = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'
botao_enviar = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'

#FUNÇÕES

def login():
    options1 = webdriver.ChromeOptions()
    options1.add_argument(r"user-data-dir={}".format('C:/CacheWpp'))
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=options1)
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, imagem_entrada)))
    driver.quit()

def enviar(destino, arquivo):
    options1 = webdriver.ChromeOptions()
    options1.add_argument(r"user-data-dir={}".format('C:/CacheWpp'))
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=options1)
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, imagem_entrada)))
    driver.find_element(By.XPATH, caixa_pesquisa_contatos).send_keys(destino)
    sleep(3)
    driver.find_element(By.XPATH, caixa_pesquisa_contatos).send_keys(Keys.ENTER)
    sleep(2)
    driver.find_element(By.XPATH, clips_anexos).click()
    sleep(5)
    driver.find_element(By.XPATH, anexo_imagem).send_keys(f'{arquivo}.jpg')
    sleep(4)
    driver.find_element(By.XPATH, botao_enviar).click()
    sleep(5)
    driver.quit()

def looping():
    for envio in lista_envio:
        try:
            enviar(envio[0], envio[1])
        except Exception as err:
            print(err)

login()
looping()
