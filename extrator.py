import os  # Módulo para interação com o sistema operacional.
import requests  # Módulo para fazer requisições HTTP.
import json  # Módulo para manipulação de dados JSON.
import yaml  # Módulo para lidar com arquivos YAML.

# Função para criar um diretório se ele não existir.
def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Função para carregar dados de um arquivo YAML.
def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

# Função para salvar dados em formato JSON em um arquivo.
def save_json(data, file_path):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

# Função para fazer uma requisição à API do OMIE.
def omie_api_request(endpoint, call, params, app_key, app_secret):
    # Constrói a URL completa para a chamada à API do OMIE.
    url = f"https://app.omie.com.br/api/v1/{endpoint}"
    headers = {'Content-Type': 'application/json'}  # Define o cabeçalho da requisição como JSON.
    # Constrói os dados da requisição.
    data = {
        "call": call,
        "app_key": app_key,
        "app_secret": app_secret,
        "param": [params]
    }
    # Envia a requisição POST para a API do OMIE.
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # Retorna os dados da resposta convertidos para JSON.
    return response.json()

# Função principal do programa.
def main():
    # Cria o diretório "JSON" se ele não existir.
    create_directory_if_not_exists("JSON")
    
    # Carrega as autorizações do arquivo YAML.
    autorizacoes = load_yaml("autorizacoes.yaml")
    OMIE_APP_KEY = autorizacoes['OMIE_APP_KEY']
    OMIE_APP_SECRET = autorizacoes['OMIE_APP_SECRET']
    
    # Carrega os parâmetros do arquivo YAML.
    parametros = load_yaml("parametros.yaml")
    # Carrega as rotas do arquivo YAML.
    rotas = load_yaml("rotas.yaml")
    
    # Itera sobre cada rota definida no arquivo "rotas.yaml".
    for rota in rotas['rotas']:
        endpoint, call = rota
        # Faz a chamada à API do OMIE e obtém os dados da resposta.
        response_data = omie_api_request(endpoint, call, parametros, OMIE_APP_KEY, OMIE_APP_SECRET)
        # Salva os dados da resposta em um arquivo JSON.
        save_json(response_data, f"JSON/{call}.json")
        # Exibe uma mensagem indicando que os dados foram salvos.
        print(f"Dados da chamada {call} salvos em JSON/{call}.json")

# Verifica se o script está sendo executado diretamente.
if __name__ == "__main__":
    main()  # Chama a função principal do programa.
