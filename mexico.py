from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapData import ScrapData

class Mexico:
    #inicializa clase
    def __init__(self, driver, pagetoscrape="", nameexcel="FileName"):
        #inicializa las variables de la clase que se usaran en la misma
        self.pageToScrape = pagetoscrape
        self.nameExcel = nameexcel
        self.country = "mex"
        #self.browser = browser.lower()
        self.driver = driver
        """# Inicializa el navegador
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Browser must be 'chrome' or 'firefox'")"""

    #hace el scrape para los datos de mexico
    def scrape_mexico_data(self):
        self.driver.get(self.pageToScrape)
        #instancia la clase de Scrap Data  y le pasa las variables necesarias
        scraping_data = ScrapData(self.driver, self.pageToScrape, self.nameExcel)

        # Espera hasta que aparezca la tabla de información
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'table'))
        )

        # Encuentra las tablas de información dentro de la pagina
        tables = self.driver.find_elements(By.TAG_NAME, "table")
        data_excel = []
        #recorre cada tabla
        count_table = 1
        for table in tables:
            try:
                #busca el tag name caption para ver el titulo de la tabla
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'caption'))
                )
                caption_element = table.find_element(By.TAG_NAME, "caption")
            except Exception as e:
                # busca el tag name th para ver el titulo de la tabla
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'th'))
                )
                caption_element = table.find_element(By.TAG_NAME, "th")
            #recupera el titulo de la tabla
            table_title = caption_element.text
            # verifica si el titulo de la tabla es correspondiente a las tablas que queremos procesar
            if table_title == "Entidades federativas de México por superficie, población y densidad" or table_title == "Población histórica de México":
                # hace el llamado de la clase que hace el scraping en el metodo de traer la informacion de la tabla y la agrega a la data que sera enviada al excel
                data_excel.append(scraping_data.get_data_table(table, table_title, count_table))
                #contador para identificar que tablas se han procesado de las 3 que se necesitan
                count_table = count_table + 1
        #retorna la data que se va a ir al excel
        return data_excel
