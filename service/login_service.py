from wikipedia.login import Login_wikipedia

def login(username_login, password):
    try:
        loginWikiPedia = Login_wikipedia("chrome", username_login, password)
        username, driver = loginWikiPedia.loginWiki()
        return username, driver
    except Exception as e:
        print(f"Error en login_service : {e}")

