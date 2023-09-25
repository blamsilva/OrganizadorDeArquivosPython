import os

import datetime

# Busca a data atual do sistema
data = datetime.date.today()
ano = data.year
mes = data.month
if mes < 10:
    mes = "0" + str(mes)
anoMesAtual = str(ano) + str(mes)

# Importa a função que abre janela para selecionar a pasta
from tkinter.filedialog import askdirectory 

# Abre uma Janela e seleciona uma pasta para ser organizada
caminho_procura = askdirectory(title="Selecione uma pasta")

# Termo que vai ser procurado
contador = int(anoMesAtual)
termo_procura = anoMesAtual

# Enquanto for diferente de data fim de busca no nome dos arquivos faça:
while termo_procura != "200501":
    for  raiz, deretorios, arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            if termo_procura in arquivo:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                if not os.path.exists(f"{caminho_procura}/{termo_procura}"):
                    os.mkdir(f"{caminho_procura}/{termo_procura}")
                #realoca o arquivo na pasta criada de acordo com a data especificada no nome
                os.rename(f"{caminho_procura}/{arquivo}", f"{caminho_procura}/{termo_procura}/{arquivo}")
    # Ciclo dos Anos
    if termo_procura[4] == "0" and termo_procura[5] == "1":
        contador -= 89
        termo_procura = str(contador)  # atualiza a váriável
    # Ciclo dos Meses
    else:
        contador -= 1#Diminui o termo procurado em -1 para variar o meses
        termo_procura = str(contador)# atualiza a váriável
