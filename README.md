# Automação de Cadastro de Produtos

Este projeto automatiza o cadastro de produtos em um sistema web a partir de um arquivo CSV, utilizando Python, Selenium e PySide6 para interface gráfica.

## Funcionalidades

- Interface gráfica para seleção do arquivo de produtos (.csv)
- Leitura e validação dos dados do arquivo
- Preenchimento automático do formulário web de cadastro de produtos
- Cadastro de múltiplos produtos de forma automatizada

## Pré-requisitos

- Python 3.8 ou superior instalado
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome (adicione ao PATH do sistema)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Antoniosvj/automacao_cadastro_produtos.git
   cd automacao
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como usar

1. Execute o arquivo principal:
   ```bash
   python main.py
   ```

2. Na interface gráfica, clique em **"Cadastro de Produtos"** e selecione o arquivo CSV com os produtos.

3. O sistema abrirá o navegador, preencherá e enviará o formulário para cada produto do arquivo.

## Formato do arquivo CSV

O arquivo CSV deve conter as seguintes colunas (com estes nomes exatos):

- Código do Produto
- Descrição
- Preço de Compra
- Quantidade em Estoque
- Preço de Venda

Exemplo:
```csv
Código do Produto;Descrição;Preço de Compra;Quantidade em Estoque;Preço de Venda
001;Produto A;10.50;100;15.00
002;Produto B;20.00;50;30.00
```

## Observações

- Certifique-se de que o arquivo `index.html` esteja sendo servido localmente (por exemplo, usando a extensão Live Server do VS Code).
- O ChromeDriver deve estar instalado e disponível no PATH do sistema.
- O navegador será aberto automaticamente durante o processo.

## Licença

Este projeto é apenas para fins educacionais.
