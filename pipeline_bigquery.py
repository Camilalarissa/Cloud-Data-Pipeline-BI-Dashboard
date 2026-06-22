import os
import requests
from bs4 import BeautifulSoup
from google.cloud import bigquery
from google.api_core.exceptions import NotFound

# 1. Autenticação na Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credenciais.json"
cliente = bigquery.Client()

# 2. Configuração do BigQuery 
PROJETO_ID = "scraping-para-bigquery" 
DATASET_ID = f"{PROJETO_ID}.dados_ecommerce"
TABELA_ID = f"{DATASET_ID}.produtos"

print("☁️ A preparar a base de dados no BigQuery...")

# 3. Criar Dataset e Tabela automaticamente se não existirem
dataset = bigquery.Dataset(DATASET_ID)
dataset.location = "US"
try:
    cliente.get_dataset(DATASET_ID)
except NotFound:
    cliente.create_dataset(dataset)
    print(f"✅ Dataset '{DATASET_ID}' criado.")

esquema = [
    bigquery.SchemaField("titulo", "STRING"),
    bigquery.SchemaField("preco", "FLOAT"),
    bigquery.SchemaField("disponibilidade", "STRING")
]
tabela = bigquery.Table(TABELA_ID, schema=esquema)
try:
    cliente.get_table(TABELA_ID)
except NotFound:
    cliente.create_table(tabela)
    print(f"✅ Tabela '{TABELA_ID}' criada.")

# 4. Extração de Dados (Web Scraping)
print("\n🕷️ A iniciar a extração de dados da loja...")
url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
resposta = requests.get(url)
sopa = BeautifulSoup(resposta.text, "html.parser")

produtos_extraidos = []
livros = sopa.find_all("article", class_="product_pod")

for livro in livros:
    titulo = livro.h3.a["title"]
    # Limpa o preço 
    preco_texto = livro.find("p", class_="price_color").text.replace("£", "").replace("Â", "")
    preco = float(preco_texto)
    disponibilidade = livro.find("p", class_="instock availability").text.strip()
    
    produtos_extraidos.append({
        "titulo": titulo,
        "preco": preco,
        "disponibilidade": disponibilidade
    })

print(f"✅ Foram extraídos {len(produtos_extraidos)} produtos.")

# 5. Carga de Dados (Envio para o BigQuery)
print("\n🚀 A enviar dados para a Google Cloud...")
erros = cliente.insert_rows_json(TABELA_ID, produtos_extraidos)

if not erros:
    print(" SUCESSO! Dados enviados para o BigQuery perfeitamente.")
else:
    print("Erros ao enviar dados:", erros)