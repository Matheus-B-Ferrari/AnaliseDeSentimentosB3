import os
import feedparser
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

HEADERS = {'User-Agent': 'Mozilla/5.0'}
NOTICIAS = []

def limpa_texto(paragrafos, limite_palavras=1000):
    """Concatena parágrafos e limita a N palavras."""
    texto = ' '.join(p.get_text(strip=True) for p in paragrafos)
    palavras = texto.split()
    return ' '.join(palavras[:limite_palavras])

# RSS Genérico (Exame e Infomoney)
def scrape_rss(fonte, feed_url):
    print(f"\n=== Coletando {fonte} (via RSS) ===")
    feed = feedparser.parse(feed_url)
    print(f"[{fonte}] {len(feed.entries)} notícias disponíveis no feed.")

    for entry in feed.entries:
        link = entry.link
        titulo = entry.title

        try:
            resp = requests.get(link, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(resp.content, 'html.parser')
            paragrafos = soup.find_all('p')
            if not paragrafos:
                continue
            texto = limpa_texto(paragrafos)

            NOTICIAS.append({
                'url': link,
                'data': datetime.now().strftime('%Y-%m-%d'),
                'titulo': titulo,
                'texto': texto,
                'fonte': fonte
            })

            time.sleep(1)
        except Exception as e:
            print(f"[{fonte}] Erro ao processar {link}: {e}")

# Valor Econômico via SCRAPING
def scrape_valor(paginas=3):
    print("\n=== Coletando Valor Econômico (scraping) ===")
    links = set()
    for i in range(1, paginas + 1):
        url = f'https://valor.globo.com/ultimas-noticias/index/feed/pagina-{i}'
        resp = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(resp.content, 'html.parser')
        h2_tags = soup.find_all('h2', class_='feed-post-link')
        for h2 in h2_tags:
            a = h2.find('a', href=True)
            if a and 'valor.globo.com' in a['href'] and not a['href'].endswith(('.pdf', '.jpg', '.png')):
                links.add(a['href'])
        time.sleep(1)

    for link in list(links):
        try:
            resp = requests.get(link, headers=HEADERS, timeout=10)
            soup = BeautifulSoup(resp.content, 'html.parser')
            titulo_tag = soup.find('h1')
            if not titulo_tag:
                continue
            titulo = titulo_tag.get_text(strip=True)
            paragrafos = soup.find_all('p')
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

            time.sleep(1)
        except Exception as e:
            print(f"[Valor] Erro ao processar {link}: {e}")

# EXECUTA TODOS
scrape_rss('Exame', 'https://exame.com/feed/')
scrape_rss('Infomoney', 'https://www.infomoney.com.br/feed/')
scrape_valor(paginas=3)

# SALVA CSV
df = pd.DataFrame(NOTICIAS)
hoje = datetime.now().strftime('%Y-%m-%d')
base_dir = os.path.dirname(os.path.abspath(__file__))  # diretório do script
output_dir = os.path.join(base_dir, 'noticias')
os.makedirs(output_dir, exist_ok=True)
df.to_csv(os.path.join(output_dir, f'noticias_{hoje}.csv'), index=False, encoding='utf-8')
print(f"\nTotal de notícias coletadas: {len(NOTICIAS)} (salvas em noticias_{hoje}.csv)")