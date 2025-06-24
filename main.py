from selenium.webdriver.remote.webelement import WebElement
from tkinter import messagebox
from PyPDF2 import PdfReader
import pygetwindow as gw
from pathlib import Path
from pyperclip import copy
from time import sleep
import atuadorWeb
import keyboard
import re
import os


nfs_sem_protoc = []


if len(os.listdir("NFS")) == 0:
    messagebox.showerror("Erro!", "A pasta NFS precisa estar com todos os arquivos PDFs das notas fiscais antes de começar.")
    raise Exception("Faltou anexar as NFS na pasta")


interagente = atuadorWeb.Interagente()

interagente.abrir_pagina_web("https://portaldenotas.claro.com.br/irj/portal")

interagente.interagir_pagina_web(endereco=("xpath", '/html/body/span/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div/form/table[1]/tbody/tr[2]/td[2]/input'), acao="Escrever", texto="************")
    
interagente.interagir_pagina_web(endereco=("xpath", '/html/body/span/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div/form/table[1]/tbody/tr[3]/td[2]/input'), acao="Escrever", texto="**********")

interagente.interagir_pagina_web(endereco=("xpath", '/html/body/span/table/tbody/tr[2]/td[2]/table/tbody/tr/td[3]/table/tbody/tr[2]/td/div/form/table[1]/tbody/tr[5]/td[2]/input'), acao="Clicar")


while True:
    try:
        interagente.interagir_pagina_web(endereco=("xpath", '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr/td[2]/div[2]/div[2]/table/tbody/tr/td[4]'), acao="Esperar")
        break
    except:
        pass

interagente.interagir_pagina_web(endereco=("xpath", '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr/td[2]/div[2]/div[2]/table/tbody/tr/td[4]'), acao="Clicar")


interagente.migrar_ao_frame(acao="ir", id="ivuFrm_page0ivu2")
interagente.migrar_ao_frame(acao="ir", id="isolatedWorkArea")

interagente.interagir_pagina_web(endereco=("xpath", '/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td/span[2]'), acao="Clicar")


for arq in os.listdir("NFS"):

    caminho_absoluto = str(Path("NFS").resolve())
    caminho_arq = caminho_absoluto + "\\" + arq
    reader = PdfReader(caminho_arq)

    numero_nf = arq.split(".")[0]
    pagina = reader.pages[0]
    texto = pagina.extract_text().upper().replace(" ", "")
    dt_emissao = re.search(r'DATADAEMISSÃODANOTA\s+(\d{2}/\d{2}/\d{4})', texto).group(1)


    try:
        protocolo = re.search(r"PROTOCOLO\d{10}", texto).group()
    except AttributeError:
        nfs_sem_protoc.append(numero_nf)
        continue


    protocolo = re.sub(r"[^\d]", "", protocolo)


    interagente.interagir_pagina_web(endereco=("xpath", '/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/span/input'), acao="Escrever", texto=protocolo)

    interagente.interagir_pagina_web(endereco=("xpath", '/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div/table/tbody/tr/td/span[1]/a'), acao="Clicar")
    sleep(0.3)

    while True:
        try:
            interagente.interagir_pagina_web(endereco=("id", 'aaaa.MonitorPrefaturaView.InfoComple_editor.0'), acao="Clicar")
            break
        except:
            continue

    interagente.migrar_ao_frame(acao="voltar")
    interagente.migrar_ao_frame(acao="ir", id="URLSPW-0")

    while True:
        try:
            interagente.interagir_pagina_web(endereco=("xpath", '/html/body/table/tbody/tr/td/div/div[1]/div/div[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/span/span/img'), acao="Clicar")
            break
        except:
            continue


    interagente.interagir_pagina_web(endereco=("id", "aaaa.InfoComplementaresView.FileUpload_PDF1-r"), acao="Clicar")

    while True:
        janela = gw.getWindowsWithTitle("Abrir")
        if janela:
            break
        sleep(0.2)


    copy(caminho_arq)

    sleep(0.5)

    keyboard.press_and_release('ctrl+v')

    sleep(0.3)

    keyboard.press_and_release(['tab']*2)
    keyboard.press_and_release('enter')

    sleep(0.3)

    interagente.interagir_pagina_web(endereco=("id", "aaaa.InfoComplementaresView.InputField_NumeroNF"), acao="Escrever", texto=numero_nf)

    interagente.interagir_pagina_web(endereco=("id", "aaaa.InfoComplementaresView.InputField_SerieNF"), acao="Escrever", texto="02")

    interagente.interagir_pagina_web(endereco=("id", "aaaa.InfoComplementaresView.InputField_DataEmissaoNF"), acao="Escrever", texto=dt_emissao)    

    interagente.interagir_pagina_web(endereco=("xpath", "/html/body/table/tbody/tr/td/div/div[1]/div/div[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr/td[1]/div/span[1]/a"), acao="Clicar")

    interagente.migrar_ao_frame(acao="voltar")

    aux = 0
    while True:
        frame_aberto = interagente.interagir_pagina_web(endereco=("id", "URLSPW-0"), acao="Retornar elemento", texto=None, limitar_espera=False, limitar_retorno=True)
        inuse = frame_aberto.get_attribute("inuse")
        aux+=1
        if aux == 30:
            interagente.migrar_ao_frame(acao="ir", id="URLSPW-0")
            interagente.interagir_pagina_web(endereco=("xpath", "/html/body/table/tbody/tr/td/div/div[1]/div/div[3]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr/td[1]/div/span[1]/a"), acao="Clicar")
            interagente.migrar_ao_frame(acao="voltar")
            aux = 0
            continue
        if inuse == "true":
            sleep(0.2)
        else:
            break


    interagente.migrar_ao_frame(acao="ir", id="ivuFrm_page0ivu2")
    interagente.migrar_ao_frame(acao="ir", id="isolatedWorkArea")


messagebox.showinfo("Trabalho finalizado", "Trabalho finalizado com sucesso!\n\nFavor, exclua os arquivos da pasta NFS para que possa dar espaço para novas notas fiscais.")
