from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Etimologia:
    # inicializa clase
    def __init__(self, browser='chrome'):
        # inicializa las variables de la clase que se usaran en la misma
        self.browser = browser.lower()
        # Inicializa el navegador
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Browser must be 'chrome' or 'firefox'")

    def get_etimology(self):
        # Encontrar el elemento que contiene el título de la sección de Etimología
        WebDriverWait(self.driver, 20).until(
            #EC.presence_of_element_located((By.XPATH, "//span[@id='Etimología']"))
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        h2_titles = self.driver.find_elements(By.TAG_NAME, "h2")
        for h2title in h2_titles:
            if h2title.text == "Etimología":
                etimologia_parrafo = h2title.find_element(By.XPATH, "//following-sibling::p")
                print(f"Etimologia parrafo {etimologia_parrafo.text}")
                break

        """etimologia_titulo = self.driver.find_element(By., "//span[@id='Etimología']")

        etimologia_titulo = self.driver.find_element(By.XPATH, "//span[@id='Etimología']")
        # Encontrar todos los elementos <p> después del título de Etimología
        etimologia_parrafo = etimologia_titulo.find_element(By.XPATH, "//following-sibling::p")"""


        # Inicializar una lista para almacenar el texto de la etimología
        #etimologia_texto = []

        # Recorrer cada elemento <p> y extraer el texto
        #for parrafo in etimologia_parrafos:
        #    etimologia_texto.append(parrafo.text)

        # Combinar el texto de todos los elementos en una cadena
        #texto_completo = ' '.join(etimologia_texto)

        # Imprimir el texto de la sección de etimología
        #print(texto_completo)