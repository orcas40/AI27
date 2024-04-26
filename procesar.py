from service.login_service import login
from service.scrape_service import scrape

if __name__ == "__main__":

    username = "Orcas40"
    password = "Otr4Contr4$1"
    browser_used = "chrome"

    countries = [
                { "country": "mex",
                  "url_target": "https://es.wikipedia.org/wiki/Anexo:Entidades_federativas_de_M%C3%A9xico_por_superficie,_poblaci%C3%B3n_y_densidad",
                  "name_excel": "DataWikipedia_mexico"},
                { "country": "usa",
                  "url_target": "https://es.wikipedia.org/wiki/Estado_de_los_Estados_Unidos",
                  "name_excel": "DataWikipedia_usa"}
              ]
    try:
        user_recover, driver = login(username, password)
        if user_recover != "":
            for country in countries:
                country_select = country["country"]
                url_select = country["url_target"]
                name_excel_select = country["name_excel"]

                scrape(driver, url_select, name_excel_select, country_select)
        else:
            print("Usuario o contraseña incorrectos")
    except Exception as e:
        raise ValueError(f"Error : {e}")