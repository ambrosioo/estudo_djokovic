import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

# Configurações do navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# URL da página
url = "https://www.flashscore.com.br/jogador/novak-djokovic/AZg49Et9/resultados/"

# Abrindo a página
driver.get(url) 

# Esperando até que o botão de aceitar cookies seja carregado
try:
    accept_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*
                                                                             ]')))
    accept_btn.click()
except:
    print("Botão de aceitar cookies não encontrado.")

for _ in range(3):
    try:
        # Esperando até que o botão "Mostrar mais jogos" seja clicável
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="live-table"]/div[1]/div[2]/div/a'))).click()
    except:
        print("Botão 'Mostrar mais jogos' não encontrado ou não clicável.")
        break
    time.sleep(2)

# Obtendo o HTML da página
html = driver.page_source

# Parseando o conteúdo HTML
soup = BeautifulSoup(html, "html.parser")

# Encontrando todos os elementos com IDs que começam com "g_2_"
ids = [element["id"][4:] for element in soup.find_all(id=lambda x: x and x.startswith("g_2_"))]

# Lista para armazenar os dados das partidas
dados_partidas = []

# Loop sobre os IDs das partidas
for id_partida in ids:
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

