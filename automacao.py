#importações
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def cadastro_produtos(file_name, url='http://127.0.0.1:5500/index.html'):

    produtos = pd.DataFrame() #cria o dataframe vazio

    try:
        #lendo arquivo
        produtos = pd.read_csv(file_name, delimiter=';')

        #renomeando colunas para facilitar o preenchimento
        produtos = produtos.rename(columns={
            'Código do Produto': 'codigo',
            'Descrição': 'descricao',
            'Preço de Compra': 'p_compra',
            'Quantidade em Estoque': 'estoque',
            'Preço de Venda': 'p_venda' 
        })
        print(f'Arquivo {file_name} lido e processado com sucesso')
    except FileNotFoundError:
        print(f'Erro: Arquivo {file_name} não encontrado')
        return False #indica falha
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')
        return False
    
    if produtos.empty:
        print('Nenhum produto encontrado no arquivo para cadastrar.')
        return False
    
    web = None
    try:
        #abre o navegador
        web = webdriver.Chrome()

        #abre a página
        web.get(url)

        #espera a pagina carregar (espera pelo botao cadastrar)
        WebDriverWait(web, 15).until(
            EC.visibility_of_all_elements_located((By.ID, 'cadastrar'))
        )
        print('Pagina de cadastro carregada')

        for _, produto in produtos.iterrows():
            codigo = web.find_element(By.NAME, 'codigo')
            codigo.clear()
            codigo.send_keys(str(produto['codigo']))

            descricao = web.find_element(By.NAME, 'descricao')
            descricao.clear()
            descricao.send_keys(str(produto['descricao']))

            p_compra = web.find_element(By.NAME, 'p_compra')
            p_compra.clear()
            p_compra.send_keys(str(produto['p_compra']))

            estoque = web.find_element(By.NAME, 'estoque')
            estoque.clear()
            estoque.send_keys(str(produto['estoque']))

            p_venda = web.find_element(By.NAME, 'p_venda')
            p_venda.clear()
            p_venda.send_keys(str(produto['p_venda']))

            btn_click = web.find_element(By.ID, 'cadastrar')
            btn_click.click()

            time.sleep(1) #espera de 1 segundo

        print('Cadastro de todos os produtos concluido com sucesso.')
        return True #indica sucesso
    except Exception as e:
        print('Ocorreu um erro inesperado durante o cadastro: {e}')
        return False
    finally:
        if web:
            web.quit() #fecha o navegador
            print('Navegador fechado')

