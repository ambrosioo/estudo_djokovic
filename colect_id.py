from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
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

for _ in range(1):
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
ids = [element["id"] for element in soup.find_all(id=lambda x: x and x.startswith("g_2_"))]

# Criando um DataFrame pandas com os IDs
df = pd.DataFrame({"IDs": ids})

# Salvando os IDs em uma planilha Excel
df.to_excel("ids_flashscore.xlsx", index=False)

# Fechando o navegador
driver.quit()

print("IDs salvos com sucesso em 'ids_flashscore.xlsx'.")
