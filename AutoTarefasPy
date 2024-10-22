import requests
import pandas as pd
from datetime import datetime

# Configurações da API
API_URL = 'https://api.example.com/data' 
API_KEY = 'sua_api_key' 

# Função para obter dados da API
def fetch_data():
    headers = {
        'Authorization': f'Bearer {API_KEY}',  
        'Content-Type': 'application/json',
    }
    
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json()  
    else:
        print(f'Erro ao buscar dados: {response.status_code}')
        return None

# Função para gerar relatórios personalizados
def generate_report(data):
    df = pd.DataFrame(data)
    
    # Processa os dados conforme necessário
    # Exemplo: Filtrar por status
    filtered_df = df[df['status'] == 'ativo']  

    # Salva o relatório em um arquivo CSV
    report_name = f'relatorio_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    filtered_df.to_csv(report_name, index=False)
    print(f'Relatório gerado: {report_name}')

# Função principal
def main():
    print('Buscando dados da API...')
    data = fetch_data()
    
    if data:
        print('Gerando relatório...')
        generate_report(data)

if __name__ == '__main__':
    main()
