#importações
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

#lendo arquivo
produtos = pd.read_csv('produtos.csv', delimiter=';')

#renomeando colunas para facilitar o preenchimento
produtos = produtos.rename(columns={
    'Código do Produto': 'codigo',
    'Descrição': 'descricao',
    'Preço de Compra': 'p_compra',
    'Quantidade em Estoque': 'estoque',
    'Preço de Venda': 'p_venda' 
})


#abre o navegador
web = webdriver.Chrome()

#abre a página
web.get('http://127.0.0.1:5500/index.html')

#espera a pagina carregar
time.sleep(5)

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

    time.sleep(2)


web.quit() #fecha o navegador