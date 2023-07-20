import os
import barcode
from barcode import EAN13
from barcode.writer import ImageWriter

def gerar_codigo_de_barras(numero, nome_arquivo):
    try:
        # Criar um objeto de código de barras EAN-13
        codigo_barras = EAN13(numero, writer=ImageWriter())

        # Salvar o código de barras no arquivo de imagem no caminho especificado
        codigo_barras.save(nome_arquivo)

        print(f"Código de barras gerado com sucesso. Arquivo: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao gerar o código de barras: {e}")

# Cria a pasta "arquivos_01" se ela ainda não existir
caminho_pasta = "arquivos_01" #nome da pasta que será salva as imagens
if not os.path.exists(caminho_pasta):
    os.makedirs(caminho_pasta)

codigo = 100110012001 #numero inicial 
cont = 0 
total = 100 #quantidade de imagens salvas
while cont < total:
    print(codigo)
    numero_codigo = str(codigo)
    nome_arquivo_saida = os.path.join(caminho_pasta, f'img_{codigo}.png')
    gerar_codigo_de_barras(numero_codigo, nome_arquivo_saida)
    codigo += 15
    cont += 1
