from google.cloud import bigquery
import os

# 1. Aponta para o ficheiro de credenciais que acabou de descarregar
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credenciais.json"

# 2. Inicializa o cliente do BigQuery
try:
    cliente = bigquery.Client()
    
    # Faz uma consulta de teste simples para ver se responde
    query = "SELECT 'Conexão com a Google Cloud realizada com sucesso!' as mensagem"
    resultado = cliente.query(query).result()
    
    for linha in resultado:
        print("✅", linha.mensagem)
        
except Exception as e:
    print("Erro ao conectar:", e)