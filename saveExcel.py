from selenium import webdriver
import xlsxwriter

class SaveExcel:
    def __init__(self, driver, dataToSave=[], nameFileExcel=""):
        # inicializa las variables de la clase que se usaran en la misma
        self.dataToSave = dataToSave
        self.nameFileExcel = nameFileExcel
        self.driver = driver
        # Inicializa el navegador
        """if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Browser must be 'chrome' or 'firefox'")"""

    #guarda los datos en excel
    def save_data_excel(self):
        # Crea el libro excel (archivo) nameFileExcel
        libro = xlsxwriter.Workbook(f'{self.nameFileExcel}.xlsx')
        datosSheet = []
        countSheet = 1
        # De los datos genera las hojas que se mostraran en excel
        for sheetData in self.dataToSave:
            datosSheet.append((f"Tabla_{countSheet}", sheetData))
            countSheet = countSheet + 1

        # recorre todas cada una de las hojas y las agrega
        for nameSheet, sheetData in datosSheet:
            # Agregar una hoja al libro
            AddSheet = libro.add_worksheet(nameSheet)

            # Escribir los datos en la hoja
            for row, dataRow in enumerate(sheetData):
                for column, valueData in enumerate(dataRow):
                    AddSheet.write(row, column, valueData)

        # Cierra el libro de Excel
        libro.close()