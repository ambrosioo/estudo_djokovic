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
    accept_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
    accept_btn.click()
except:
    print("Botão de aceitar cookies não encontrado.")

for _ in range(0):
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
        aces_jogador_1 = driver.find_element(By.XPATH, '//div[contains(@class, "_row_n1rcj_9")]//strong[text()="Aces"]/ancestor::div[@class="_row_n1rcj_9"]/div[@class="_value_bwnrp_5 _homeValue_bwnrp_10"]').text
    except NoSuchElementException:
        aces_jogador_1 = ""
    try:
        aces_jogador_2 = driver.find_element(By.XPATH, '//div[contains(@class, "_row_n1rcj_9")]//strong[text()="Aces"]/ancestor::div[@class="_row_n1rcj_9"]/div[@class="_value_bwnrp_5 _awayValue_bwnrp_14"]').text
    except NoSuchElementException:
        aces_jogador_2 = ""
    try:
        duplas_faltas_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[3]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        duplas_faltas_jogador_1 = ""
    try:
        duplas_faltas_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[3]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        duplas_faltas_jogador_2 = ""
    try:
        percentual_primeiro_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[4]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        percentual_primeiro_servico_jogador_1 = ""
    try:
        percentual_primeiro_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[4]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        percentual_primeiro_servico_jogador_2 = ""
    try:
        pontos_ganhos_primeiro_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[5]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        pontos_ganhos_primeiro_servico_jogador_1 = ""
    try:
        pontos_ganhos_primeiro_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[5]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        pontos_ganhos_primeiro_servico_jogador_2 = ""
    try:
        pontos_ganhos_segundo_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[5]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        pontos_ganhos_segundo_servico_jogador_1 = ""
    try:
        pontos_ganhos_segundo_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[6]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        pontos_ganhos_segundo_servico_jogador_2 = ""
    try:
        break_points_salvos_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[7]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        break_points_salvos_jogador_1 = ""
    try:
        break_points_salvos_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[7]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        break_points_salvos_jogador_2 = ""
    try:
        pontos_de_retorno_primeiro_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[2]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        pontos_de_retorno_primeiro_servico_jogador_1 = ""
    try:
        pontos_de_retorno_primeiro_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[2]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        pontos_de_retorno_primeiro_servico_jogador_2 = ""
    try:
        pontos_de_retorno_segundo_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[3]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        pontos_de_retorno_segundo_servico_jogador_1 = ""
    try:
        pontos_de_retorno_segundo_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[3]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        pontos_de_retorno_segundo_servico_jogador_2 = ""
    try:
        break_points_vencidos_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[4]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        break_points_vencidos_jogador_1 = ""
    try:
        break_points_vencidos_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[4]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        break_points_vencidos_jogador_2 = ""
    try:
        winners_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[2]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        winners_jogador_1 = ""
    try:
        winners_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[2]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        winners_jogador_2 = ""
    try:
        erros_nao_forcados_jogador_1 = EC.visibility_of_element_located(By.XPATH, '//strong[contains(text(), "Erros Não Forçados")]/parent::div/following-sibling::div//strong').text
    except NoSuchElementException:
        erros_nao_forcados_jogador_1 = ""

    try:
        erros_nao_forcados_jogador_2 = driver.find_element(By.XPATH, '//div[contains(@class, "_row_n1rcj_9")]//strong[text()="Erros Não Forçados"]/ancestor::div[@class="_row_n1rcj_9"]/div[@class="_value_bwnrp_5 _awayValue_bwnrp_14"]').text
    except NoSuchElementException:
        erros_nao_forcados_jogador_2 = ""
    try:
        pontos_vencidos_na_rede_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[4]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        pontos_vencidos_na_rede_jogador_1 = ""
    try:
        pontos_vencidos_na_rede_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[4]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        pontos_vencidos_na_rede_jogador_2 = ""
    try:
        maximo_de_pontos_em_sequencia_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[5]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        maximo_de_pontos_em_sequencia_jogador_1 = ""
    try:
        maximo_de_pontos_em_sequencia_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[5]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        maximo_de_pontos_em_sequencia_jogador_2 = ""
    try:
        pontos_de_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[6]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        pontos_de_servico_jogador_1 = ""
    try:
        pontos_de_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[6]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        pontos_de_servico_jogador_2 = ""
    try:
        pontos_de_retorno_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[7]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        pontos_de_retorno_jogador_1 = ""
    try:
        pontos_de_retorno_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[7]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        pontos_de_retorno_jogador_2 = ""
    try:
        maximo_de_games_em_sequencia_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[2]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        maximo_de_games_em_sequencia_jogador_1 = ""
    try:
        maximo_de_games_em_sequencia_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[2]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        maximo_de_games_em_sequencia_jogador_2 = ""
    try:
        games_como_sacador_vencido_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[3]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        games_como_sacador_vencido_jogador_1 = ""
    try:
        games_como_sacador_vencido_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[3]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        games_como_sacador_vencido_jogador_2 = ""
    try:
        games_como_recebedor_vencido_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[4]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        games_como_recebedor_vencido_jogador_1 = ""
    try:
        games_como_recebedor_vencido_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[4]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        games_como_recebedor_vencido_jogador_2 = ""
    try:
        total_games_vencidos_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[5]/div[1]/div[1]/strong').text
    except NoSuchElementException:
        total_games_vencidos_jogador_1 = ""
    try:
        total_games_vencidos_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[5]/div[1]/div[3]/strong').text
    except NoSuchElementException:
        total_games_vencidos_jogador_2 = ""

    # Armazenar os dados em um dicionário
    dados_partida = {
        'ID Partida': id_partida,
        'Jogador 1': jogador_1,
        'Jogador 2': jogador_2,
        'Data da Partida': data_partida,
        'Aces do Jogador 1': aces_jogador_1,
        'Aces do Jogador 2': aces_jogador_2,
        'Duplas Faltas do Jogador 1': duplas_faltas_jogador_1,
        'Duplas Faltas do Jogador 2': duplas_faltas_jogador_2,
        'Percentual Primeiro Serviço do Jogador 1': percentual_primeiro_servico_jogador_1,
        'Percentual Primeiro Serviço do Jogador 2': percentual_primeiro_servico_jogador_2,
        'Pontos Ganhos Segundo Serviço do Jogador 1': pontos_ganhos_segundo_servico_jogador_1,
        'Pontos Ganhos Segundo Serviço do Jogador 2': pontos_ganhos_segundo_servico_jogador_2,
        'Break Points Salvos do Jogador 1': break_points_salvos_jogador_1,
        'Break Points Salvos do Jogador 2': break_points_salvos_jogador_2,
        'Pontos de Retorno Primeiro Serviço do Jogador 1': pontos_de_retorno_primeiro_servico_jogador_1,
        'Pontos de Retorno Primeiro Serviço do Jogador 2': pontos_de_retorno_primeiro_servico_jogador_2,
        'Pontos de Retorno Segundo Serviço do Jogador 1': pontos_de_retorno_segundo_servico_jogador_1,
        'Pontos de Retorno Segundo Serviço do Jogador 2': pontos_de_retorno_segundo_servico_jogador_2,
        'Break Points Vencidos do Jogador 1': break_points_vencidos_jogador_1,
        'Break Points Vencidos do Jogador 2': break_points_vencidos_jogador_2,
        'Winners do Jogador 1': winners_jogador_1,
        'Winners do Jogador 2': winners_jogador_2,
        'Erros Não Forçados do Jogador 1': erros_nao_forcados_jogador_1,
        'Erros Não Forçados do Jogador 2': erros_nao_forcados_jogador_2,
        'Pontos Vencidos na Rede do Jogador 1': pontos_vencidos_na_rede_jogador_1,
        'Pontos Vencidos na Rede do Jogador 2': pontos_vencidos_na_rede_jogador_2,
        'Máximo de Pontos em Sequência do Jogador 1': maximo_de_pontos_em_sequencia_jogador_1,
        'Máximo de Pontos em Sequência do Jogador 2': maximo_de_pontos_em_sequencia_jogador_2,
        'Pontos de Serviço do Jogador 1': pontos_de_servico_jogador_1,
        'Pontos de Serviço do Jogador 2': pontos_de_servico_jogador_2,
        'Pontos de Retorno do Jogador 1': pontos_de_retorno_jogador_1,
        'Pontos de Retorno do Jogador 2': pontos_de_retorno_jogador_2,
        'Máximo de Games em Sequência do Jogador 1': maximo_de_games_em_sequencia_jogador_1,
        'Máximo de Games em Sequência do Jogador 2': maximo_de_games_em_sequencia_jogador_2,
        'Games como Sacador Vencido do Jogador 1': games_como_sacador_vencido_jogador_1,
        'Games como Sacador Vencido do Jogador 2': games_como_sacador_vencido_jogador_2,
        'Games como Recebedor Vencido do Jogador 1': games_como_recebedor_vencido_jogador_1,
        'Games como Recebedor Vencido do Jogador 2': games_como_recebedor_vencido_jogador_2,
        'Total de Games Vencidos do Jogador 1': total_games_vencidos_jogador_1,
        'Total de Games Vencidos do Jogador 2': total_games_vencidos_jogador_2,
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

