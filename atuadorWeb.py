from selenium import webdriver   
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class Interagente:
    """
    Classe para interagir com páginas web usando Selenium WebDriver.
    Permite navegar em páginas, preencher campos, esperar por elementos, e outras interações.
    """

    def __init__(self):
        pass


    def abrir_pagina_web(self, link):
        servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=servico)
        self.driver.get(link)
        self.driver.maximize_window()



    def interagir_pagina_web(self, endereco, acao, texto=None, limitar_espera=False, limitar_retorno=False, timeout=60):
        """
        Realiza ações em um elemento da página web, como clicar, escrever ou retornar o próprio elemento.

        Parâmetros:
            xpath (str): O XPath do elemento a ser encontrado.
            acao (str): A ação a ser executada. Pode ser "Clicar", "Escrever", "Retornar elemento" ou "Esperar".
            texto (str, opcional): Texto a ser inserido caso a ação seja "Escrever".
            limitar_espera (bool, opcional): Limita o tempo de espera para encontrar o elemento.
            limitar_retorno (bool, opcional): Limita o número de tentativas de encontrar o elemento.

        Retorna:
            WebElement ou None: Retorna o elemento se a ação for "Retornar elemento", caso contrário retorna None.
        """

        tipo, identificador = endereco
        if tipo == "xpath":
            tipo = By.XPATH
        elif tipo == "id":
            tipo = By.ID

        try:
            if limitar_espera:
                tempo = 7.5
            if limitar_retorno:
                tempo = 2.5 
            else:
                tempo = timeout

            elemento = WebDriverWait(self.driver, tempo).until(
                EC.presence_of_element_located((tipo, identificador))
            )

            match acao:
                case "Clicar":
                    elemento.click()
                case "Escrever":
                    elemento.clear()
                    sleep(0.8)
                    elemento.send_keys(texto)
                case "Retornar elemento":
                    return elemento
                case "Esperar":
                    pass

        except TimeoutException:
            print(f"[ERRO] Elemento não encontrado ou ação '{acao}' falhou para elemento: {identificador}")
            return None



    def migrar_ao_frame(self, acao, id=None):
        match acao:
            case "ir":
                iframe = WebDriverWait(self.driver, 25).until(
                    EC.presence_of_element_located((By.ID, id))
                )
                self.driver.switch_to.frame(iframe)

            case "voltar":
                self.driver.switch_to.default_content()
