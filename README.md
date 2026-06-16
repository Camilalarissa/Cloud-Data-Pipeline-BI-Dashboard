# Cloud Data Pipeline & BI Dashboard

<div align="center">
  <img src="https://img.shields.io/badge/Google_Cloud-BigQuery-%234285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="BigQuery">
  <img src="https://img.shields.io/badge/Looker_Studio-Dashboard-%234285F4?style=for-the-badge&logo=looker&logoColor=white" alt="Looker">
  <img src="https://img.shields.io/badge/Python-Automation-%23704214?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</div>

---

## Objetivo de Negócio

Desenvolvimento de uma solução de **Engenharia de Dados ponta a ponta** para monitorização de e-commerce. O objetivo foi automatizar a extração de dados da concorrência e centralizá-los num armazém de dados em nuvem, permitindo a criação de relatórios estratégicos em tempo real.

## O Pipeline

1. **Extração:** Script Python (Selenium/BeautifulSoup) realiza o _web scraping_ de catálogos de produtos.
2. **Armazenamento:** Os dados são tratados e enviados via API para o **Google BigQuery**, garantindo escalabilidade e segurança.
3. **Visualização:** Dashboards dinâmicos construídos no **Looker Studio**, permitindo análise de preços e stock de forma visual.

## Tecnologias Utilizadas

- **Cloud:** Google Cloud Platform (BigQuery).
- **Processamento:** Python (`google-cloud-bigquery`, `requests`, `BeautifulSoup`).
- **BI:** Looker Studio.

---

## Valor para o Cliente

Esta solução permite que o cliente tome decisões de preços baseadas em dados reais da concorrência, reduzindo o tempo de análise manual e eliminando erros de relatórios em folha de cálculo. **Estou disponível para adaptar este pipeline a qualquer fonte de dados específica do seu negócio.**
