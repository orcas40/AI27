from wikipedia.mexico import Mexico
from wikipedia.usa import USA
from excel.saveExcel import SaveExcel


def scrape(driver, page_to_script, name_excel, country="mex"):
    try:
        if country == "mex":
            wikiDataMexico = Mexico(driver, page_to_script, name_excel)
            data_to_excel = wikiDataMexico.scrape_mexico_data()

        if country == "usa":
            wikiDataUsa = USA(driver, page_to_script, name_excel)
            data_to_excel =wikiDataUsa.scrape_usa_data()

        save_data_to_excel = SaveExcel(driver, data_to_excel, name_excel)
        save_data_to_excel.save_data_excel()
    except Exception as e:
        print(f"Error en scrape_service : {e}")
    finally:
        pass