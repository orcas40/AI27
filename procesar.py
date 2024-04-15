from loginWikipedia import LoginWikipedia
from mexico import Mexico
from usa import USA
from saveExcel import SaveExcel

def scrape_data_info(driver, page_to_script, name_excel, country="mex"):
    if country == "mex":
        wikiDataMexico = Mexico(driver, page_to_script, name_excel)
        data_to_excel = wikiDataMexico.scrape_mexico_data()

    if country == "usa":
        wikiDataUsa = USA(driver, page_to_script, name_excel)
        data_to_excel =wikiDataUsa.scrape_usa_data()

    save_data_to_excel = SaveExcel(driver, data_to_excel, name_excel)
    save_data_to_excel.save_data_excel()

if __name__ == "__main__":

    username = "Orcas40"
    password = "Kldnpdlvkm$1"
    login = LoginWikipedia("chrome", username, password)
    user_recover, driver = login.loginWiki()
    if user_recover != "":

        #nombre del excel para mexico
        nameExcelFileMex = f'DataWikipedia_mexico'
        #pagina para hace el scrape de mexico
        page_to_script = 'https://es.wikipedia.org/wiki/Anexo:Entidades_federativas_de_M%C3%A9xico_por_superficie,_poblaci%C3%B3n_y_densidad'
        # ejecuta la funcion que inicia el scrape para mexico
        scrape_data_info(driver, page_to_script, nameExcelFileMex, "mex")

        # nombre del excel para usa
        nameExcelFileUsa = f'DataWikipedia_usa'
        # pagina para hace el scrape de USA
        page_to_script = 'https://es.wikipedia.org/wiki/Estado_de_los_Estados_Unidos'
        # ejecuta la funcion que inicia el scrape para USA
        scrape_data_info(driver, page_to_script, nameExcelFileUsa, "usa")

    else:
        print(f"Usuario o contraseña incorrectos")
        raise ValueError("Usuario o contraseña incorrectos")