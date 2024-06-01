import os  # Importa o módulo os para interação com o sistema operacional.
import requests  # Importa o módulo requests para fazer requisições HTTP.
import json  # Importa o módulo json para manipulação de dados JSON.
import yaml  # Importa o módulo yaml para lidar com arquivos YAML.

# Criar a pasta "JSON" se não existir
if not os.path.exists("JSON"):  # Verifica se a pasta "JSON" não existe.
    os.makedirs("JSON")  # Cria a pasta "JSON" se não existir.

# Carregar as autorizações do arquivo YAML
with open("autorizacoes.yaml", "r") as file:  # Abre o arquivo "autorizacoes.yaml" em modo de leitura.
    autorizacoes = yaml.safe_load(file)  # Carrega o conteúdo do arquivo YAML para o dicionário "autorizacoes".

OMIE_APP_KEY = autorizacoes['OMIE_APP_KEY']  # Obtém a chave de aplicativo do OMIE do dicionário "autorizacoes".
OMIE_APP_SECRET = autorizacoes['OMIE_APP_SECRET']  # Obtém o segredo de aplicativo do OMIE do dicionário "autorizacoes".

# Carregar os parâmetros do arquivo YAML
with open("parametros.yaml", "r") as file:  # Abre o arquivo "parametros.yaml" em modo de leitura.
    parametros = yaml.safe_load(file)  # Carrega o conteúdo do arquivo YAML para o dicionário "parametros".

# Carregar as rotas do arquivo YAML
with open("rotas.yaml", "r") as file:  # Abre o arquivo "rotas.yaml" em modo de leitura.
    rotas = yaml.safe_load(file)  # Carrega o conteúdo do arquivo YAML para o dicionário "rotas".

endpoint_base = "https://app.omie.com.br/api/v1/"  # Define a URL base para as chamadas à API do OMIE.

# Função para fazer a chamada para a API do OMIE
def omie_api_request(endpoint, call, params):
    url = endpoint_base + endpoint  # Monta a URL completa para a chamada à API do OMIE.
    headers = {
        'Content-Type': 'application/json',  # Define o cabeçalho da requisição como JSON.
    }
    data = {
        "call": call,  # Define o tipo de chamada para a API.
        "app_key": OMIE_APP_KEY,  # Adiciona a chave de aplicativo do OMIE aos dados da requisição.
        "app_secret": OMIE_APP_SECRET,  # Adiciona o segredo de aplicativo do OMIE aos dados da requisição.
        "param": [params]  # Adiciona os parâmetros específicos da chamada à API.
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))  # Envia a requisição POST para a API do OMIE.
    response_data = response.json()  # Converte a resposta da requisição para JSON.
    
    # Salvar o JSON dentro da pasta "JSON" com o nome da chamada
    with open(f"JSON/{call}.json", "w") as json_file:  # Abre o arquivo JSON correspondente à chamada em modo de escrita.
        json.dump(response_data, json_file, indent=4)  # Escreve os dados da resposta JSON no arquivo.
    
    return response_data  # Retorna os dados da resposta da API do OMIE.

# Exemplo de como usar a função para uma rota específica
for rota in rotas['rotas']:  # Itera sobre cada rota definida no arquivo "rotas.yaml".
    endpoint, call = rota  # Separa o endpoint e o tipo de chamada para a API.
    params = parametros  # Define os parâmetros a serem passados para a chamada à API.
    response_data = omie_api_request(endpoint, call, params)  # Faz a chamada à API do OMIE.
    # Processar o response_data se necessário
    print(f"Dados da chamada {call} salvos em JSON/{call}.json")  # Exibe uma mensagem indicando que os dados foram salvos.
