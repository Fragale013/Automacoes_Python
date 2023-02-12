#Olá, o código abaixo é uma proposta altamente escalável para envio de imagens via Whatsapp para contatos ou grupos já conhecidos pela sua conta Whatsapp
#É extremamente útil para envio de dashboards e prints de relatórios de tempos em tempos para contatos ou grupos desejados
# Esse código serve apenas para testes de automação e não sugiro que seja utilizado em ambientes de produção
# Para ambientes de produção existem APIs específicas que devem ser contratadas para essa finalidade
# Os elementos mapeados na tela da WEB Whatsapp costumam mudar de tempos em tempos, estarei disponibilizando novas versões assim que identificar essas mudanças
#Atualização  12/02/2023


#O código abaixo utiliza a tecnologia selenium para emular o envio de imagens via navegador google Chrome para os destinos desejados
#Para isso é necessário instalar as bibliotecas:
#webdriver_manager > Irá automatizar o download das novas versões do chromedriver
#selenium > utilizaremos a função webdriver do selenium para emular o envio das mensagens no navegador


##Dito isso, vamos ao código :D

##################################################


#Começamos importando as bibliotecas
#IMPORTANTE: O arquivo DisparoWppDestinos é onde você vai editar os contatos que irão receber as imagens e os contatos ou grupos de destino
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from DisparoWppDestinos import lista_envio


#Nessa etapa iremos definir as variáveis utilizadas nas funções, atualmente os elementos interagíveis na tela estão mapeados via XPATH com os endereçáveis abaixo
url = 'https://web.whatsapp.com/'
imagem_entrada = '//*[@id="app"]/div/div/div[3]/header/div[1]'
caixa_pesquisa_contatos = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
caixa_mensagem = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
clips_anexos = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
anexo_imagem = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input'
botao_enviar = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'


#Aqui vamos declarar as funções que serão chamadas na aplicação:

##################################################
#Primeiramente vamos criar uma função para login, ela ficará parada na tela de código QR por 30 segundos para aguardar o primeiro login
#Não se preocupe, com a função user-data-dir, não será necessário fazer o login toda a vez, porque isso tornaria a automação inviável
#Atualmente não há restrição de tempo em que uma sessão fica ativa no web-whatsapp, porém há o limite de 4 dispositivos na conta padrão do whatsapp
#Dessa forma, certifique-se que há pelo menos 1 posição disponível nos dispositivos conectados na sua conta
def login():
    options1 = webdriver.ChromeOptions()
    options1.add_argument(r"user-data-dir={}".format('C:/CacheWpp'))
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=options1)
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, imagem_entrada)))
    driver.quit()
##################################################
    
##################################################
#Agora vamos criar a função que irá de fato realizar o envio, ela deve abrir a sessão criada pela função de login e iniciar o envia da imagem
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
##################################################
    
    
##################################################
#Por fim, deve haver uma rotina de looping, onde o código percorrerá a lista importada do arquivo DisparoWppDestinos e realizar a função de envio para cada item dessa lista
def looping():
    for envio in lista_envio:
        try:
            enviar(envio[0], envio[1])
        except Exception as err:
            print(err)
#Caso ele econtre qualquer problema no envio, irá exibir o erro na tela antes de prosseguir para o próximo envio
##################################################


##################################################
#Por fim, finalmente a chamada das funções, essas duas linhas abaixo são as realmente "colocam" o código para rodar
login()
looping()
##################################################
