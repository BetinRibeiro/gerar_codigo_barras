import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def agrupar_imagens_em_pdf(pasta_origem, nome_pdf_saida):
    try:
        # Lista todos os arquivos da pasta
        arquivos = os.listdir(pasta_origem)

        # Filtra somente os arquivos de imagem (PNG, JPEG e JPG)
        imagens = [arquivo for arquivo in arquivos if arquivo.lower().endswith(('.png', '.jpg', '.jpeg'))]

        if not imagens:
            print("Nenhuma imagem encontrada na pasta.")
            return

        # Ordena as imagens por ordem alfabética (se quiser outra ordem, basta modificar a função sorted())
        imagens = sorted(imagens)

        # Configurações do PDF
        largura_pagina, altura_pagina = letter
        largura_imagem, altura_imagem = largura_pagina / 4, altura_pagina / 6
        total_imagens_por_pagina = 24

        # Gera o PDF com as imagens
        pdf = canvas.Canvas(nome_pdf_saida, pagesize=letter)

        for indice, imagem in enumerate(imagens, 1):
            caminho_imagem = os.path.join(pasta_origem, imagem)
            img = Image.open(caminho_imagem)

            # Calcula as coordenadas para posicionar a imagem na página
            coluna = (indice - 1) % 4
            linha = (total_imagens_por_pagina - 1 - (indice - 1) // 4) % 6
            x = largura_imagem * coluna
            y = altura_imagem * linha

            # Ajusta as dimensões da imagem para o tamanho da célula
            img.thumbnail((largura_imagem, altura_imagem))

            # Adiciona a imagem à página do PDF
            pdf.drawInlineImage(caminho_imagem, x, y, width=img.width, height=img.height)

            # Verifica se é hora de criar uma nova página
            if indice % total_imagens_por_pagina == 0:
                pdf.showPage()

        # Finaliza o PDF
        pdf.save()

        print(f"PDF gerado com sucesso. Arquivo: {nome_pdf_saida}")

    except Exception as e:
        print(f"Erro ao gerar o PDF: {e}")

# Exemplo de uso da função
pasta_especifica = "arquivos_01"  # Substitua pelo caminho da pasta desejada
nome_pdf_saida = "newnew_arquivo.pdf"  # Substitua pelo nome do arquivo PDF de saída

agrupar_imagens_em_pdf(pasta_especifica, nome_pdf_saida)
