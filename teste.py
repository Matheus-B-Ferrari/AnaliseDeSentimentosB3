import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HEADERS = {'User-Agent': 'Mozilla/5.0'}
NOTICIAS = []

def limpa_texto(paragrafos, limite_palavras=1000):
    texto = ' '.join([p.get_text(strip=True) for p in paragrafos])
    palavras = texto.split()
    return ' '.join(palavras[:limite_palavras])

# G1 com paginação
def scrape_g1(paginas=5):
    print("Coletando G1...")
    links = set()
    for i in range(1, paginas + 1):
        url = f'https://g1.globo.com/economia/index/feed/pagina-{i}.ghtml'
        resp = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(resp.content, 'html.parser')
        novos_links = [a['href'] for a in soup.find_all('a', href=True)
                       if '/economia/' in a['href'] and not a['href'].endswith(('.pdf', '.jpg', '.png'))]
        links.update(novos_links)
        time.sleep(1)

    for link in list(links)[:100]:
        try:
            r = requests.get(link, headers=HEADERS)
            s = BeautifulSoup(r.content, 'html.parser')
            titulo_tag = s.find('h1')
            if not titulo_tag:
                continue
            titulo = titulo_tag.get_text(strip=True)
            paragrafos = s.find_all('p')
            if not paragrafos:
                continue
            texto = limpa_texto(paragrafos)
            NOTICIAS.append({
                'url': link,
                'data': datetime.now().strftime('%Y-%m-%d'),
                'titulo': titulo,
                'texto': texto,
                'fonte': 'G1'
            })
            time.sleep(1.5)
        except Exception as e:
            print(f"[G1] Erro: {e}")

# Valor Econômico com paginação
def scrape_valor(paginas=5):
    print("Coletando Valor Econômico...")
    links = set()
    for i in range(1, paginas + 1):
        url = f'https://valor.globo.com/ultimas-noticias/index/feed/pagina-{i}'
        resp = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(resp.content, 'html.parser')
        h2_tags = soup.find_all('h2', class_='feed-post-link')
        for h2 in h2_tags:
            a = h2.find('a', href=True)
            if a and 'valor.globo.com' in a['href']:
                links.add(a['href'])
        time.sleep(1)

    for link in list(links)[:100]:
        try:
            r = requests.get(link, headers=HEADERS)
            s = BeautifulSoup(r.content, 'html.parser')
            titulo_tag = s.find('h1')
            if not titulo_tag:
                continue
            titulo = titulo_tag.get_text(strip=True)
            paragrafos = s.find_all('p')
            if not paragrafos:
                continue
            texto = limpa_texto(paragrafos)
            NOTICIAS.append({
                'url': link,
                'data': datetime.now().strftime('%Y-%m-%d'),
                'titulo': titulo,
                'texto': texto,
                'fonte': 'Valor Econômico'
            })
            time.sleep(1.5)
        except Exception as e:
            print(f"[Valor] Erro: {e}")

# Infomoney com Selenium (carregar mais)
def scrape_infomoney_selenium(noticias_limite=100):
    print("Coletando Infomoney com Selenium...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.infomoney.com.br/ultimas-noticias/")
    time.sleep(3)

    # Clicar várias vezes no botão "Carregar mais"
    try:
        for _ in range(10):
            button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Carregar mais")]'))
            )
            driver.execute_script("arguments[0].click();", button)
            time.sleep(2)
    except:
        pass  # Acabou os posts

    # Coletar os links das notícias
    links = set()
    cards = driver.find_elements(By.TAG_NAME, 'a')
    for card in cards:
        href = card.get_attribute('href')
        if href and 'infomoney.com.br' in href and not href.endswith(('.pdf', '.jpg', '.png')):
            links.add(href)

    driver.quit()

    # Visitar cada link coletado
    for link in list(links)[:noticias_limite]:
        try:
            r = requests.get(link, headers=HEADERS)
            s = BeautifulSoup(r.content, 'html.parser')
            titulo_tag = s.find('h1')
            if not titulo_tag:
                continue
            titulo = titulo_tag.get_text(strip=True)
            paragrafos = s.find_all('p')
            if not paragrafos:
                continue
            texto = limpa_texto(paragrafos)
            NOTICIAS.append({
                'url': link,
                'data': datetime.now().strftime('%Y-%m-%d'),
                'titulo': titulo,
                'texto': texto,
                'fonte': 'Infomoney'
            })
            time.sleep(1.5)
        except Exception as e:
            print(f"[Infomoney] Erro: {e}")

# Execução
scrape_g1(paginas=5)
scrape_valor(paginas=5)
scrape_infomoney_selenium(noticias_limite=100)

# Exportar CSV
df = pd.DataFrame(NOTICIAS)
df.to_csv('noticias.csv', index=False, encoding='utf-8')
print(f"{len(NOTICIAS)} notícias salvas com sucesso em 'noticias.csv'.")
