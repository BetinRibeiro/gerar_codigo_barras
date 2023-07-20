# gerar_codigo_barras
gerar_codigo_barras


Para utilizar as duas funções agrupar_imagens_em_pdf() e gerar_codigo_de_barras(), você precisará das seguintes dependências:

    os: Biblioteca padrão do Python para interagir com o sistema operacional.
    barcode: Biblioteca para gerar códigos de barras.
    Pillow: Biblioteca para manipulação de imagens.
    reportlab: Biblioteca para geração de arquivos PDF.

# Instalar a biblioteca para gerar códigos de barras
pip install python-barcode

# Instalar a biblioteca para manipulação de imagens
pip install Pillow

# Instalar a biblioteca para geração de PDFs
pip install reportlab


import os
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
