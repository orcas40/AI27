from selenium.webdriver.common.by import By

class ScrapData:
    def __init__(self, driver, pageToScrape="", nameExcel="FileName", language="es"):
        # inicializa las variables de la clase que se usaran en la misma
        self.pageToScrape = pageToScrape
        self.nameExcel = nameExcel
        self.language = language
        self.driver = driver

    def get_data_for_state(self, h2s_data, text_to_find):
        #column.find_element(By.TAG_NAME, "a").click()
        # busca los elementos con titulos en la pagina de informacion del estado
        #h2s_data = self.driver.find_elements(By.TAG_NAME, "h2")
        state_data = f"No tiene {text_to_find}"
        for h2 in h2s_data:
            # verifica si el titulo es el correcto
            if h2.text == f"{text_to_find}[editar código · editar]":
                # busca el siguente parrafo despues del titulo
                info_parrafo = h2.find_element(By.XPATH, "./following-sibling::p")
                # asigna el valor del texto del parrafo
                state_data = info_parrafo.text

        return state_data

    #trae los datos de la fila ya sea del theader th o del tbody td mediante la variable thortd
    def get_data_rows(self, info_table, thortd, count_table, index_column ):
        rowsData = []
        rows = info_table.find_elements(By.TAG_NAME, "tr")
        count_row_proces = 0
        for row in rows:
            # Obtener todas las celdas de la fila
            cells = row.find_elements(By.TAG_NAME, thortd)
            data_row = []
            for cell in cells:
                # Extraer el texto de la celda y agregarlo a la lista de datos de la fila
                data_row.append(cell.text)


            if count_table == 3:
                if count_row_proces == 1:
                    data_row.append("Toponimia")

                count_row_proces = count_row_proces + 1
                if len(cells)>2:
                    if cells[index_column].text != "Entidad":
                        cells[index_column].find_element(By.TAG_NAME, "a").click()
                        # busca los elementos con titulos en la pagina de informacion del estado
                        h2s_data = self.driver.find_elements(By.TAG_NAME, "h2")
                        toponimia_data = self.get_data_for_state(h2s_data, "Toponimia")
                        data_row.append(toponimia_data)
                        self.driver.back()

            rowsData.append(data_row)

        return rowsData



    #trae solo los datos de una columna y el indice es un parametro para identificar que columna desea procesar
    def get_data_rows_one_column(self, info_table, thortd ,index_column):
        rowsData = []
        rows = info_table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            # Obtener todas las celdas de la fila
            cells = row.find_elements(By.TAG_NAME, thortd)
            data_row = []
            etimologia_data = "No tiene etimología"
            try:
                # verifica si es solo el titulo de la columna
                if thortd == "th":
                    # agrega el titulo de la columna
                    etimologia_data = "Etimología"
                # verifica si es solo el dato de la columna
                if thortd == "td":
                    # encuentra el elemento link y da click para ir a la pagina de la informacion del estado
                    cells[index_column].find_element(By.TAG_NAME, "a").click()
                    # busca los elementos con titulos en la pagina de informacion del estado
                    h2s_data = self.driver.find_elements(By.TAG_NAME, "h2")
                    etimologia_data = self.get_data_for_state(h2s_data, "Etimología")
                    self.driver.back()
            except Exception as e:
                self.driver.back()
                etimologia_data = "No tiene etimología"

            # agrega los valores de la columna de estado y etimologia
            data_row.append(cells[index_column].text)
            data_row.append(etimologia_data)

            # agrega los datos a la fila
            rowsData.append(data_row)

        return rowsData



    # Recupera los datos de la tabla para mexico y valida si los titulos de la tabla corresponden a los que se desean recuperar
    def get_data_table(self, table, tableTitle, count_table, index_column= 1):
        dataRowsRecover = []
        #valida si el titulo de la tabla para entidades federativas
        if tableTitle == "Entidades federativas de México por superficie, población y densidad":
            # encuentra el elemento tbody en la tabla en turno
            info_table = table.find_element(By.TAG_NAME, 'tbody')
            print(f"Processing ...")
            # Ejecuta el llamado de datos de las filas y cada columna
            dataRowsRecover = self.get_data_rows(info_table ,"td", count_table, index_column)
        # valida si el titulo de la tabla para poblacion historica
        elif tableTitle == "Población histórica de México":
            #recupera los titulos de la tabla del thead
            info_table = table.find_element(By.TAG_NAME, 'thead')
            dataRowsRecover1 = self.get_data_rows(info_table, "th", count_table, index_column)
            #recupera los datos de la tabla del tbody
            info_table = table.find_element(By.TAG_NAME, 'tbody')
            dataRowsRecover2 = self.get_data_rows(info_table, "td", count_table, index_column)
            #une los datos recuperados de los titulos y los datos de la tabla
            dataRowsRecover = dataRowsRecover1 + dataRowsRecover2

        return dataRowsRecover

    # Recupera los datos de la tabla para usa
    def get_data_table_usa(self, table):
        dataRowsRecover = []
        # recupera los titulos de la tabla del thead
        info_table = table.find_element(By.TAG_NAME, 'thead')
        dataRowsRecover1 = self.get_data_rows_one_column(info_table, "th", 1)
        #recupera los datos de la tabla del tbody
        info_table = table.find_element(By.TAG_NAME, 'tbody')
        dataRowsRecover2 = self.get_data_rows_one_column(info_table, "td", 1)
        # une los datos recuperados de los titulos y los datos de la tabla
        dataRowsRecover = dataRowsRecover1 + dataRowsRecover2

        return dataRowsRecover
