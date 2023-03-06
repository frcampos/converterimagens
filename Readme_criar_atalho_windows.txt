Notas sobre a instalação e uso da aplicação de conversão de ficheiros

A aplicação converte para a resolução configurável no ficheiro config.ini
as imagens que se colocam de forma não comprimidas e com a melhor resolução possível, sendo colocadas previamente na
pasta /data/naocomprimida.
O sistema utiliza um processo de duas camadas de compressão e rescalonamento da imagem.
De referir que a imagem não comprimida, deve ter a melhor resolução possível e a relação entre a largura da imagem
e a sua altura o mais próxima possível da imagem final.

A partir do ficheiro "config.ini" é possível alterar as configurações de onde se localizam as imagem, a nivel da fonte e do destino.
No entanto é necessário alguma cautela, uma vez que se não for encontrado pela aplicação o ficheiro a converter 
não será possível a realização da conversão.

Para correr aplicaçao é necessário preparar o ambiente de trabalho, começando por instalar o python e depois instalar o modulo pillow.
1- Descarregar o Python a partir do link : https://www.python.org/downloads/
2- Após a instalação com sucesso e em modo comando escrever pip install pillow. Deverá instalar o pacote pillow.

Após a instalação dos componentes é necessário instalar numa pasta especifica o ficheiro zip, criado para o efeito que contem uma imagem para 
teste assim como a programação "main.py" e o ficheiro de configuração "config.ini". Contem ainda as pastas e subpastas onde
ficarão os ficheiros de imagem.

 


Após a instalação deve-se preparar para criar um atalho no ambiente de trabalho, caso de pretenda sistematizar a operação:

Pré-verificação


3- fazer unzip para uma pasta que o utilizador tenha direitos de escrita
Abrir nessa pasta e descomprimir o ficheiro main.cy, config.ini e pasta data e subpastas de acordo com o configurado em config.ini.

4- aconselhado ter pelo menos um ficheiro a ter na pasta "data/naocomprimido" ou mesmo vários ficheiros de teste e pasta de 
imagens de acordo com o configurado em "config.ini".

5- através do comando  cd  localizar a pasta onde se encontra o ficheiro mai.py e config.py.

6- Confirmar que existe a pasta data-> naocomprimido

7- Correr na linha de comandos na pasta onde foi descompactado o ficheiro main.py 

 python -m main.cy
 
deve ser testado antes de realizar o atalho, que a aplicação está a fazer a respetiva conversão.
 
Criar Atalho:
 
Para criar atalho, após descompressao numa determinada PASTA
 
Para criar um atalho no Windows que execute o script Python "main.py", siga estas etapas:

8- Clique com o botão direito do mouse em uma área vazia da área de trabalho e selecione "Novo" e depois "Atalho".

9- Na janela de criação de atalho, digite o caminho completo para o interpretador Python que você deseja usar, seguido do caminho completo para o arquivo "main.py". Por exemplo, se o Python estiver instalado em "C:\Python38\python.exe" e o arquivo "main.py" estiver localizado em "C:\Users\SeuNome\Documents\ProjetoPython", você deve digitar:

python


10- Quando da criação do atalho no deskTop, inclouir a linha de comando:

"C:\Users\frcam\AppData\Local\Programs\Python\Python311\python.exe" "C:\Users\frcam\utils\main.py"

11- Clique em "Avançar" e digitar nome para o atalho, como "ConversoImagens", por exemplo.

12- Clique em "Concluir" para criar o atalho.

13- Clique com o botão direito do rato no atalho recém-criado e selecione "Propriedades".

14- Após a criação deverá estar configurado no atalho algo semelhante a :

Destino

C:\Users\frcam\AppData\Local\Programs\Python\Python311\python.exe "C:\Users\frcam\utils\main.py"

Iniciar em:

C:\Users\frcam\AppData\Local\Programs\Python\Python311



15- Na guia "Atalho", pode-se personalizar o atalho, alterando o ícone, definindo as teclas de atalho, etc.

16- Na guia "Compatibilidade", é possivel definir as configurações de compatibilidade para o atalho.

17- Na guia "Destino",  verificar e editar o caminho do arquivo que será executado quando o atalho for aberto. 
Certifique-se de que o caminho do arquivo "main.py" seja o correto e que todos os caminhos de arquivos usados no script 
sejam especificados corretamente.

18- Depois de criar o atalho, basta clicar nele para executar o script Python "main.py" e converter as imagens que se encontram na pasta naocomprimido
para a pasta data/comprimidosite.


Versão 1.0 6 março 2023.
