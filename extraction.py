import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Configuração do ChromeDriver
chrome_driver_path = "caminho/para/seu/chromedriver"
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Configurações do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# Inicializar o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Lista de IDs das partidas
ids_partidas = [
    "449nysz3", "lWXVhDnI"
]

# Lista para armazenar os dados das partidas
dados_partidas = []

# Loop sobre os IDs das partidas
for id_partida in ids_partidas:
    # Construir a URL da partida
    url = f"https://www.flashscore.com.br/jogo/{id_partida}/#/resumo-de-jogo/estatisticas-de-jogo/0"
    
    # Abrir a URL no navegador
    driver.get(url)

    # Tentar clicar no botão de aceitar cookies, se estiver presente
    try:
        elemento_aceitar_cookies = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        )
        elemento_aceitar_cookies.click()
    except TimeoutException:
        pass  # Se não encontrar o botão de aceitar cookies, continua o código normalmente
    
    time.sleep(3)

# Loop sobre os IDs das partidas
for id_partida in ids_partidas:
    # Construir a URL da partida
    url_partida = f"https://www.flashscore.com.br/jogo/{id_partida}/#/resumo-de-jogo/estatisticas-de-jogo/0"
    
    # Abrir a URL no navegador
    driver.get(url_partida)

    # Tentar clicar no botão de aceitar cookies, se estiver presente
    try:
        elemento_aceitar_cookies = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        )
        elemento_aceitar_cookies.click()
    except TimeoutException:
        pass  # Se não encontrar o botão de aceitar cookies, continua o código normalmente
    
    time.sleep(3)

    def verificar_texto_elemento(elemento, texto):
        return texto in elemento.text

    # Extrair os dados dos xpath fornecidos
    try:
        jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[4]/div[2]/div[3]/div[2]/a').text
    except NoSuchElementException:
        jogador_1 = ""
    try:
        jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[4]/div[4]/div[3]/div[1]/a').text
    except NoSuchElementException:
        jogador_2 = ""
    try:
        data_partida = driver.find_element(By.XPATH, '//*[@id="detail"]/div[4]/div[1]/div').text
    except NoSuchElementException:
        data_partida = ""
    try:
        erros_nao_forcados_jogador_1 = driver.find_element(By.XPATH, '//strong[contains(text(), "Erros Não Forçados")]/parent::div/preceding-sibling::div//strong').text
    except NoSuchElementException:
        erros_nao_forcados_jogador_1 = ""
        
    try:
        erros_nao_forcados_jogador_2 = driver.find_element(By.XPATH, '//strong[contains(text(), "Erros Não Forçados")]/parent::div/following-sibling::div//strong').text
    except NoSuchElementException:
        erros_nao_forcados_jogador_2 = ""
    

    # Armazenar os dados em um dicionário
    dados_partida = {
        'ID Partida': id_partida,
        'Jogador 1': jogador_1,
        'Jogador 2': jogador_2,
        'Data da Partida': data_partida,
        'Erros Não Forçados do Jogador 1': erros_nao_forcados_jogador_1,
        'Erros Não Forçados do Jogador 2': erros_nao_forcados_jogador_2,
    }

    # Adicionar os dados da partida à lista
    dados_partidas.append(dados_partida)

# Fechar o navegador
driver.quit()

# Criar um DataFrame pandas com os dados das partidas
df = pd.DataFrame(dados_partidas)

# Salvar os dados em um arquivo Excel
df.to_excel('dados_partidas.xlsx', index=False)

print("Dados das partidas foram coletados e salvos em 'dados_partidas.xlsx'")
