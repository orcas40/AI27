from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wikipedia.scrap_data import ScrapData

class USA:
    #inicializa clase
    def __init__(self, driver, pagetoscrape="", nameexcel="FileName"):
        #inicializa las variables de la clase que se usaran en la misma
        self.pageToScrape = pagetoscrape
        self.nameExcel = nameexcel
        self.country = "usa"
        self.driver = driver

    #hace el scrape para los datos de usa
    def scrape_usa_data(self):
        self.driver.get(self.pageToScrape)
        #instancia la clase de Scrap Data  y le pasa las variables necesarias
        scraping_data = ScrapData(self.driver, self.pageToScrape, self.nameExcel)

        # Espera hasta que aparezca la tabla de información
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'wikitable'))
        )

        # Encuentra las tablas de información dentro de la pagina
        table = self.driver.find_element(By.CLASS_NAME, "wikitable")
        data_excel = []
        #si existe la tabla entonces procesa la obtencion de la informacion
        if table:
            # ejecuta el traer los datos de la tabla
            data_excel.append(scraping_data.get_data_table_usa(table))

        #retorna la data que se va a ir al excel
        return data_excel