from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credenciais.json"


try:
    cliente = bigquery.Client()
    
    
    query = "SELECT 'Conexão com a Google Cloud realizada com sucesso!' as mensagem"
    resultado = cliente.query(query).result()
    
    for linha in resultado:
        print("", linha.mensagem)
        
except Exception as e:
    print("Erro ao conectar:", e)