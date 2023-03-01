# Este é um exemplo de uma amostra em Python script, para realizar de forma
# sistemática a conversão de imagens com uma determinada resolução, normalmente retiradas de máquinas fotográfica, telemóveis
# e outros tipos de dispositivos, para a preparação de imagens a colocar em sítios web.
# Foi usado nos testes o PyCharm - help at https://www.jetbrains.com/help/pycharm/
# Assim o exemplo de script para em "batch" converter imagens em formato jpg a partir de imagens de maior resolução para colocação
# no sitio de acordo com largura e altura programavel, assim como qualidade
# Nota: No PyCharm para instalar modulos ir à opção "Terminal"
# PIL é a livraria de manipulação de imagem
# os, glob e errno é relativamente ao trabalho com ficheiros e códigos de erro do sistema Operativo
# criado por Fernando Rui Campos 13- 22 fevereiro 2023. Testes realizados com mais de 2000 imagens de diversas resoluções de
# origem, tendo como final a qualidade programada na variável valor_perc_qualidade = 75 e dimensões através das
# variáveis, resol_valor_largura = 900 e resol_valor_altura = 735.
# Os valores acima são meramente indicativos para as notícias

import PIL
import os
import glob
import errno
from PIL import Image


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('A processar script Phython para converter e otimizar imagens para a web a partir de uma pasta')

# pasta de origem onde se encontram os ficheiros a comprimir. Apenas deverá ter ficheiros de imagem
# Variaveis globais não necessita de acordo com a Linguagem Python, mas é apenas para referência da existência

global pasta_imagem
global caminho_img_nresolucao
global caminho_imgs_comprimido
global num_files_max
global valor_perc_qualidade
global resol_valor_largura
global resol_valor_altura
global ALGORITMO_RESIZED
ADD_name_file_compressed = ''
ADD_name_file_resized = ''

# Numero máximo de ficheiros a converter, se colocar valor superior ao número de ficheiros não tem qualquer efeito
# valor_perc_qualidade deve ser teóricamente ser superior a 30 e inferior a 90, dependendo do tipo de imagem
# Valor de 75 equivale a 75% de quakidade o que segundo autores não se nota alteração. No entanto em alguns casos
# e dependendo da imagem de onde se deve usar (noticias ou carroussel) a que corresponde a 400x320 ou 860x420 px
# resol_valor_largura em pixeis - px
# resol_valor_altura em pixeis  - px
# possibilidade de programação do tipo de algoritmo utilizado para a alteração da resolução
# A livraria/modulo Pillow, permite vários,  NEAREST, BOX, BILINEAR, HAMMING, BICUBIC, LANCZOS
# A constituição da variável é por exemplo  Image.Resampling.BOX ou Image.Resampling.LANCZOS
# A variável ALGORITMO_RESIZED permite alterar o tipo de algoritmo de alteração de tamanho
# Testes de largura 1350x422 no carroussel e 870x700 nas noticias , ver ppi 150 por causa dos novos equipamentos
# máximo de 150 ppi por imagem, máximo de 2626 imagens

num_files_max = 50
valor_perc_qualidade = 75
resol_valor_largura = 900
resol_valor_altura = 720
ALGORITMO_RESIZED = Image.Resampling.BICUBIC

# pasta de origem dos ficheiros antes da  compressão - "pasta_imagem"

# pasta de destino dos ficheiros após compressão
caminho_imgs_comprimido = '/Users/fernandocampos/testes/comprimidosite/'
# Caminho onde se encontram as imagens a converter. Deve ser adaptado de acordo com a configuração
pasta_imagem = '/Users/fernandocampos/testes/naocomprimido/'
caminho_img_nresolucao = '/Users/fernandocampos/testes/comprimidoresized/'
caminho_img_rescomprimido = '/Users/fernandocampos/testes/rescomprimido/'

print(f"A verificar os requisitos para conversão de imagens para a Web")
if os.path.exists(pasta_imagem):
    print(f"Existe a pasta de origem de imagens para conversão em {pasta_imagem}")
else:
    print(f"O caminho ou pasta de imagens fonte não  existe ou está em outo caminho de acordo com o definido em {pasta_imagem}. A sair...")
    exist(2)

# Obtem a lista de ficheiros de imagem
# Criação de lista com ficheiros

files = os.listdir(pasta_imagem)

# Listar todos os ficheiros e pastas utilizando a função os.listdir()

print(f'Estes são os ficheiros da diretoria corrente: {files}')
# Obter o numero de ficheiros encontrados
# atenção que a posição 0 conta!
# Criar Loop de manipulação ficheiros
# definir img_size_width e img_size_height , i.e. largura e altura da imagem

# Verifica o numero de interações pelo numero de ficheiros existentes na pasta ou entao pelo numero máximo definido em
# num_files_max enquanto variavel global
# Só pode conter ficheiros do tipo jpg

if num_files_max <= 3:
    print(
        f"Numero de ficheiros máximos introduzidos na variável num_files_max {num_files_max} é inferior ao valor minimo, a ajustar ...")
    num_files_max = 3
if valor_perc_qualidade <= 29:
    print(f" Valor de qualidade tem de ser superior ou igual a 50. a ajustar valor minimo da qualidade {valor_perc_qualidade} da imagem final para 50 ")
    valor_perc_qualidade = 50

numero_itens = len(files) - 1

if numero_itens <= 0:
    print(f"O numero de imagens existentes para processamento na pasta de origem {pasta_imagem} é inferior a 1. A sair...")
    exit(2)

if num_files_max > numero_itens + 1:
    num_files_max = numero_itens
    print(
        f"O numero de imagens para processamento programado na variável num_files_max  {num_files_max} é inferior ao existente em na pasta de origem {pasta_imagem}. A ajustar numero de ficheiros a processar ")
i = 0
while (i <= numero_itens and i <= num_files_max - 1):

    print("O ficheiro encontrado corresponde a posição", i, "da lista de ficheiros é:", files[i])
    if files[i] == '.DS_Store':
        print(f'Não processado ', files[i])
        i = i + 1
        caminho_completo_imagem = pasta_imagem + files[i]
    else:
        caminho_completo_imagem = pasta_imagem + files[i]

    image = Image.open(caminho_completo_imagem)

    # rgb_im = image.convert("RGB")
    name_file_compressed = caminho_imgs_comprimido + ADD_name_file_compressed + files[i]
    name_file_resized = caminho_img_nresolucao + ADD_name_file_resized + files[i]
    try:

        image.save(name_file_compressed, 'webp', optimize=True, quality=valor_perc_qualidade)

        img_resize = image.resize((resol_valor_largura, resol_valor_altura), ALGORITMO_RESIZED)
        img_resize.save(name_file_resized)

    except IOError as exc:

        if exc.errno == errno.ENOENT:
            print(exc.strerror)
            print("this will print")
            # handle one way
        elif exc.errno == errno.EBADF:
            print(exc.strerror)
            print("this will not print")
            # handle another way

    i = i + 1

# Vai ser aplicado a alteração para a resolução final a partir do ficheiro comprimido
# Os ficheiros encontram-se na pasta
# caminho_imgs_comprimido = '/Users/fernandocampos/testes/comprimidosite/'
# Necessário ler a pasta e aplicar o algoritmo de resize sem compressão


files_new = os.listdir(caminho_imgs_comprimido)
numero_itens = len(files_new) - 1
# Feito compensação para efeitos de simplificação quando existe ficheiro DSTORE e duas pastas não passiveis
# de serem processadas.
i = 0
# numero_itens = len(files_new) + 2
# num_files_max = num_files_max + 3
# para compensar o numero de pastas e ficheiros nao lidos

while (i <= numero_itens + 3 and i <= num_files_max - 1):

    print("O ficheiro ***comprimido*** corresponde a posição", i, "da lista de ficheiros é:", files_new[i],"em caso de sucesso é gravado na pasta ", caminho_img_rescomprimido )
    if files_new[i] == '.DS_Store' or files_new[i] == 'resized' or files_new[i] == 'rescomprimido':
        print(f'Não processado  por ser .DS_STORE ou resized, ou rescomprimido - pastas e ficheiros não processados',
              files_new[i])
        i = i + 1
        # por existirem duas pastas e 1 ficheiro não reconhecido na pasta
    else:
        caminho_completo_imagem = caminho_imgs_comprimido + files_new[i]

    caminho_completo_imagem = caminho_imgs_comprimido + files_new[i]
    image = Image.open(caminho_completo_imagem)

    # rgb_im = image.convert("RGB")
    name_file_compressed = caminho_img_rescomprimido + '' + files_new[i]

    try:

        img_resize_compressed = image.resize((resol_valor_largura, resol_valor_altura), ALGORITMO_RESIZED)

        img_resize_compressed.save(name_file_compressed)
        # comprimir , fazer testes com e sem abertura previa do ficheiro
        # image = Image.open(name_file_compressed)

        image.save(name_file_compressed, 'webp', optimize=True, quality=valor_perc_qualidade)


    except IOError as exc:

        if exc.errno == errno.ENOENT:
            print(exc.strerror)
            print("this will print")
            # handle one way
        elif exc.errno == errno.EBADF:
            print(exc.strerror)
            print("this will not print")
            # handle another way

    i = i + 1
