# Extração de Dados da API do OMIE

Este é um script Python para extrair dados da API do OMIE e salvar os resultados em arquivos JSON. Ele utiliza arquivos YAML para configurar as autorizações, parâmetros e rotas da API, proporcionando flexibilidade para adaptar a extração de dados conforme necessário.

## Requisitos

**Requests:** Este módulo é utilizado para fazer requisições HTTP. Você pode instalá-lo usando pip:

```bash
pip install requests
```

**PyYAML:** Este módulo é utilizado para manipulação de arquivos YAML. Você pode instalá-lo usando pip:
```bash
codigo: pip install PyYAML
```

## Utilização
1. Clone este repositório e navegue até o diretório onde o script está localizado.
2. Configure os arquivos YAML de acordo com suas credenciais, parâmetros e rotas desejadas.
3. Execute o script Python.

O script irá iterar sobre as rotas definidas em rotas.yaml, fazendo chamadas à API do OMIE com os parâmetros especificados em parametros.yaml. Os resultados serão salvos como arquivos JSON na pasta JSON.

## Personalização
Você pode modificar os arquivos YAML conforme necessário para se adequarem às suas necessidades de extração de dados. Isso inclui adicionar novas rotas, ajustar os parâmetros de consulta e atualizar as credenciais de autenticação.

Com essa estrutura flexível, você pode facilmente extrair diferentes conjuntos de dados da API do OMIE e adaptar o script para atender aos seus requisitos específicos.

## Configuração de autorização da API

**Autorizacoes.yaml:** Este arquivo contém as chaves de aplicativo do OMIE necessárias para autenticação na API (estou usando as chaves de teste).

```yaml
OMIE_APP_KEY: 38333295000  # Chave de aplicativo do OMIE, necessária para autenticação na API.
OMIE_APP_SECRET: fed2163e2e8dccb53ff914ce9e2f1258  # Segredo de aplicativo do OMIE, também necessário para autenticação na API.

```
## Configuração de Endpoint da API
**endpoint_base:** Define a URL base para as chamadas à API do OMIE.

```Python
endpoint_base = "https://app.omie.com.br/api/v1/"  # Define a URL base para as chamadas à API do OMIE.
```

## Configuração de rotas para chamados da API

**Rotas.yaml:** Aqui, você pode listar as rotas da API do OMIE que deseja acessar. Cada rota consiste em um endpoint e o tipo de chamada para a API.

```yaml
rotas:
  - ["geral/clientes/", "ListarClientes"]  # Rota de chamadas para listar clientes na API do OMIE.
  - ["geral/produtos/", "ListarProdutos"]  # Rota de chamadas para listar produtos na API do OMIE.
  - ["produtos/nfconsultar/", "ListarNF"]  # Rota de chamadas para consultar notas fiscais de produtos na API do OMIE.
```

## Configuração de parâmetros para chamados da API

**Parâmetros.yaml:** Neste arquivo, você pode definir os parâmetros específicos para suas consultas à API, como número de página, registros por página e outros parâmetros relevantes.

```yaml
pagina: 1  # Número da página a ser consultada na API do OMIE.
registros_por_pagina: 50  # Número de registros por página a serem retornados na consulta à API.
apenas_importado_api: "N"  # Indicador para filtrar os registros apenas se foram importados via API, inicialmente configurado como "N" (não).
```

