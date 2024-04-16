from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Caminho para o seu ChromeDriver, substitua com o seu próprio caminho
chrome_driver_path = "caminho/para/seu/chromedriver"

# Configuração do ChromeDriver
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Configurações do Chrome
url = "https://www.flashscore.com.br/jogador/novak-djokovic/AZg49Et9/resultados/"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# Inicializar o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Abrir a URL no navegador
driver.get(url)

# Esperar até que o botão de aceitar cookies seja visível e, em seguida, clicar nele
elemento_aceitar_cookies = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
)
elemento_aceitar_cookies.click()

# Encontrar todos os elementos de detalhes do jogo
elementos_detalhes_jogo = driver.find_elements(By.XPATH, '//div[@title="Clique para detalhes do jogo!"]')

# Loop sobre cada elemento de detalhes do jogo
for elemento in elementos_detalhes_jogo:
    # Clicar no elemento de detalhes do jogo
    elemento.click()
    
    # Aguardar a mudança para a nova janela
    nova_janela = driver.window_handles[-1]
    driver.switch_to.window(nova_janela)

    # Agora, clique no xpath desejado na nova janela
    elemento_xpath_nova_janela = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="detail"]/div[7]/div/a[2]/button'))
    )
    elemento_xpath_nova_janela.click()
    time.sleep(3)

    # Extrair os dados da partida
    jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[4]/div[2]/div[3]/div[2]/a').text
    jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[4]/div[4]/div[3]/div[1]/a').text
    data_partida = driver.find_element(By.XPATH, '//*[@id="detail"]/div[4]/div[1]/div').text
    aces_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[2]/div[1]/div[1]/strong').text
    aces_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[2]/div[1]/div[3]/strong').text
    duplas_faltas_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[3]/div[1]/div[1]/strong').text
    duplas_faltas_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[3]/div[1]/div[3]/strong').text
    percentual_primeiro_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[4]/div[1]/div[1]/strong').text
    percentual_primeiro_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[4]/div[1]/div[3]/strong').text
    pontos_ganhos_primeiro_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[5]/div[1]/div[1]/strong').text
    pontos_ganhos_primeiro_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[5]/div[1]/div[3]/strong').text
    pontos_ganhos_segundo_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[5]/div[1]/div[1]/strong').text
    pontos_ganhos_segundo_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[6]/div[1]/div[3]/strong').text
    break_points_salvos_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[7]/div[1]/div[1]/strong').text
    break_points_salvos_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[9]/div[7]/div[1]/div[3]/strong').text
    pontos_de_retorno_primeiro_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[2]/div[1]/div[1]/strong').text
    pontos_de_retorno_primeiro_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[2]/div[1]/div[3]/strong').text
    pontos_de_retorno_segundo_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[3]/div[1]/div[1]/strong').text
    pontos_de_retorno_segundo_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[3]/div[1]/div[3]/strong').text
    break_points_vencidos_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[4]/div[1]/div[1]/strong').text
    break_points_vencidos_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[10]/div[4]/div[1]/div[3]/strong').text
    winners_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[2]/div[1]/div[1]/strong').text
    winners_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[2]/div[1]/div[3]/strong').text
    erros_nao_forcados_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[3]/div[1]/div[1]/strong').text
    erros_nao_forcados_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[3]/div[1]/div[3]/strong').text
    pontos_vencidos_na_rede_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[4]/div[1]/div[1]/strong').text
    pontos_vencidos_na_rede_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[4]/div[1]/div[3]/strong').text
    maximo_de_pontos_em_sequencia_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[5]/div[1]/div[1]/strong').text
    maximo_de_pontos_em_sequencia_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[5]/div[1]/div[3]/strong').text
    pontos_de_servico_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[6]/div[1]/div[1]/strong').text
    pontos_de_servico_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[6]/div[1]/div[3]/strong').text
    pontos_de_retorno_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[7]/div[1]/div[1]/strong').text
    pontos_de_retorno_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[7]/div[1]/div[3]/strong').text
    total_de_pontos_ganhos_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[8]/div[1]/div[1]/strong').text
    total_de_pontos_ganhos_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[11]/div[8]/div[1]/div[3]/strong').text
    maximo_de_games_em_sequencia_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[2]/div[1]/div[1]/strong').text
    maximo_de_games_em_sequencia_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[2]/div[1]/div[3]/strong').text
    games_como_sacador_vencido_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[3]/div[1]/div[1]/strong').text
    games_como_sacador_vencido_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[3]/div[1]/div[1]/strong').text
    games_como_recebedor_vencido_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[4]/div[1]/div[1]/strong').text
    games_como_recebedor_vencido_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[4]/div[1]/div[3]/strong').text
    total_games_vencidos_jogador_1 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[5]/div[1]/div[1]/strong').text
    total_games_vencidos_jogador_2 = driver.find_element(By.XPATH, '//*[@id="detail"]/div[12]/div[5]/div[1]/div[3]/strong').text

    
    # Criar um DataFrame pandas com os dados
    dados = {
        'Jogador 1': jogador_1,
        'Jogador 2': jogador_2,
        'Data da Partida': data_partida,
        'Aces do Jogador 1': [aces_jogador_1],
        'Aces do Jogador 2': [aces_jogador_2],
        'Duplas Faltas do Jogador 1': [duplas_faltas_jogador_1],
        'Duplas Faltas do Jogador 2': [duplas_faltas_jogador_2],
        'Percentual Primeiro Serviço do Jogador 1': [percentual_primeiro_servico_jogador_1],
        'Percentual Primeiro Serviço do Jogador 2': [percentual_primeiro_servico_jogador_2],
        'Pontos Ganhos Primeiro Serviço do Jogador 1': [pontos_ganhos_primeiro_servico_jogador_1],
        'Pontos Ganhos Primeiro Serviço do Jogador 2': [pontos_ganhos_primeiro_servico_jogador_2],
        'Pontos Ganhos Segundo Serviço do Jogador 1': [pontos_ganhos_segundo_servico_jogador_1],
        'Pontos Ganhos Segundo Serviço do Jogador 2': [pontos_ganhos_segundo_servico_jogador_2],
        'Break Points Salvos do Jogador 1': [break_points_salvos_jogador_1],
        'Break Points Salvos do Jogador 2': [break_points_salvos_jogador_2],
        'Pontos de Retorno Primeiro Serviço do Jogador 1': [pontos_de_retorno_primeiro_servico_jogador_1],
        'Pontos de Retorno Primeiro Serviço do Jogador 2': [pontos_de_retorno_primeiro_servico_jogador_2],
        'Pontos de Retorno Segundo Serviço do Jogador 1': [pontos_de_retorno_segundo_servico_jogador_1],
        'Pontos de Retorno Segundo Serviço do Jogador 2': [pontos_de_retorno_segundo_servico_jogador_2],
        'Break Points Vencidos do Jogador 1': [break_points_vencidos_jogador_1],
        'Break Points Vencidos do Jogador 2': [break_points_vencidos_jogador_2],
        'Winners do Jogador 1': [winners_jogador_1],
        'Winners do Jogador 2': [winners_jogador_2],
        'Erros Não Forçados do Jogador 1': [erros_nao_forcados_jogador_1],
        'Erros Não Forçados do Jogador 2': [erros_nao_forcados_jogador_2],
        'Pontos Vencidos na Rede do Jogador 1': [pontos_vencidos_na_rede_jogador_1],
        'Pontos Vencidos na Rede do Jogador 2': [pontos_vencidos_na_rede_jogador_2],
        'Máximo de Pontos em Sequência do Jogador 1': [maximo_de_pontos_em_sequencia_jogador_1],
        'Máximo de Pontos em Sequência do Jogador 2': [maximo_de_pontos_em_sequencia_jogador_2],
        'Pontos de Serviço do Jogador 1': [pontos_de_servico_jogador_1],
        'Pontos de Serviço do Jogador 2': [pontos_de_servico_jogador_2],
        'Pontos de Retorno do Jogador 1': [pontos_de_retorno_jogador_1],
        'Pontos de Retorno do Jogador 2': [pontos_de_retorno_jogador_2],
        'Total de Pontos Ganhos do Jogador 1': [total_de_pontos_ganhos_jogador_1],
        'Total de Pontos Ganhos do Jogador 2': [total_de_pontos_ganhos_jogador_2],
        'Máximo de Games em Sequência do Jogador 1': [maximo_de_games_em_sequencia_jogador_1],
        'Máximo de Games em Sequência do Jogador 2': [maximo_de_games_em_sequencia_jogador_2],
        'Games como Sacador Vencido do Jogador 1': [games_como_sacador_vencido_jogador_1],
        'Games como Sacador Vencido do Jogador 2': [games_como_sacador_vencido_jogador_2],
        'Games como Recebedor Vencido do Jogador 1': [games_como_recebedor_vencido_jogador_1],
        'Games como Recebedor Vencido do Jogador 2': [games_como_recebedor_vencido_jogador_2],
        'Total de Games Vencidos do Jogador 1': [total_games_vencidos_jogador_1],
        'Total de Games Vencidos do Jogador 2': [total_games_vencidos_jogador_2],
    }
    
    df = pd.DataFrame(dados)
    
    # Salvar os dados em um arquivo Excel
    with pd.ExcelWriter('dados_partida.xlsx', mode='a', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, header=False)

    # Fechar a aba atual
    driver.close()
    
    # Voltar para a aba anterior
    driver.switch_to.window(driver.window_handles[0])

# Fechar o navegador
driver.quit()
