# converterimagens
Converter ficheiros de imagem a partir de fotografias  de maior resolução para converter  para web, partindo do principio 
que os níveis de equilibrio da imagem, níveis de saturação estão otimizadas.
Trata-se de um script em Python que permite a partir de variáveis configuráveis no script, a conversão de ficheiros em formato jpg de forma a diminuir a sua dimensão.
O principio será a de se colocar um ou mais ficheiros de imagem numa pasta, que após o processamento do script terá como resultado
ficheiros comprimidos através de processo de processo com utilização do algoritmo BICUBIC e tambem reformatação para a resolução final pretendida.
Um aspeto essencial para garantir a qualidade dos ficheiros finais é que o valor da variável de qualidade e da relação entre a largura da imagem a converter e 
a imagem que se pretende para a página Web. De referir que a imagem na pasta onde as imagens não estão comprimidas, devem ter uma resolução inicial superior 
à resolução final, no entanto é essencial para que a imagem resultante não seja distorcida pela diferença da resolução.
Por exemplo se na página web se pretende uma imagem que tem a sua dimensão ótima de 900x720 pixel (px), o que significa 900 px de largura
e 720 px de altura. A  relação é obtida através da divisão entre a largura e a altura, neste caso 900/720=1,25 . 
O mesmo é dizer que a largura é 25% maior que a altura. 
Neste caso e partindo de uma suposta imagem  de 3696 × 2448 px de uma máquina fotográfica NIKON D5100, para a qual é necessário a otimizar para a web,
a relação é de 1,5.
Assim dado que a relação entre a largura e altura é superior (r=1,5) à imagem de destinado (r=1,25), terá de ser realizada adaptação 
através de técnicas de tratamento de imagem de forma a que a relação da imagem a tratar seja de 1,25. Por exemplo se se pretender manter a altura da imagem
segnifica que terá de ser ajustada em largura a imagem para 3060 px (altura x 1.25 = 2448 x 1.25 = 3060). A partir desta mensagem e tendo em conta
que a relação (1.25) se terá de manter para a imagem final. 
Caso a imagem final pretendida seja de 900 px e a altura 720 px, o script terá de ser programado através da introdução dos seguintes parametros
resol_valor_largura = 900, resol_valor_altura = 720. O valor de qualidade por defeito é de 75, via configuração valor_perc_qualidade = 75,
sendo que um valor mais reduzido corresponde a maior nível de compressão mas uma menor qualidade final de imagem, dependendo no entanto do tipo de imagem,
sendo que existem imagenes convertidas  com valor de 30, com nível aceitável.
Para que o script possa processar as imagens  é necessário instalar os vários módulos do Python.
Para instalar o python ver por exemplo o sitio oficial :https://www.python.org/ .
Após instalação deve via linha de comando a partir da linha de comandos deve instalar os módulos. 
pip install os ,  pip install glob, ...
Relativamente às pastas de fonte das imagens e destino, está estruturado de forma a se poder configurar a paste fonte e as pastas  destino.
Os caminhos de exemplo:
# Caminho onde se encontram as imagens a converter. Deve ser adaptado de acordo com a configuração
pasta_imagem = '/Users/fernandocampos/testes/naocomprimido/'
# pasta de destino dos ficheiros após compressão sem necessidade de redução da resolução
caminho_imgs_comprimido = '/Users/fernandocampos/testes/comprimidosite/'
# pasta de destino dos ficheiros após compressão com necessidade de redução da resolução
caminho_img_nresolucao = '/Users/fernandocampos/testes/comprimidoresized/'
A pasta onde são armazenadas as imagens não tratadas não devem ter subpastas ou outros tipos de ficheiros, que não imagens em formato jpg.





