from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login_wikipedia:
    def __init__(self, browser='chrome', username='', password=''):
        # inicializa las variables de la clase que se usaran en la misma
        self.username = username
        self.password = password
        # Inicializa el navegador
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Browser must be 'chrome' or 'firefox'")

    def loginWiki(self, language="es"):
        try:
            login_word_link = {"es": "Acceder", "en": "Log in"}
            # Abrir la página de Wikipedia
            self.driver.get(f"https://{language}.wikipedia.org/")

            # Encontrar el enlace 'Log in' utilizando el texto del enlace
            login_link = self.driver.find_element(By.LINK_TEXT, login_word_link[language])
            try:
                login_link = self.driver.find_element(By.LINK_TEXT, "Log in")
            except:
                login_link = self.driver.find_element(By.LINK_TEXT, "Acceder")
            #hacer click en el link de Log in
            login_link.click()

            # Esperar a que aparezcan los campos de nombre de usuario y contraseña
            # encontrar el elememnto de Nombre del usuario
            username_field = self.driver.find_element(By.ID, "wpName1")
            # encontrar el elememnto de contraseña
            password_field = self.driver.find_element(By.ID, "wpPassword1")

            # Rellenar los campos de nombre de usuario y contraseña
            username_field.send_keys(self.username)
            password_field.send_keys(self.password)

            # Enviar el formulario de inicio de sesión
            password_field.send_keys(Keys.RETURN)
            #password_field.send_keys()

            # Esperar a que se cargue la página después de iniciar sesión
            self.driver.implicitly_wait(10)  # Esperar un máximo de 10 segundos para que se cargue la página

            # Obtener el nombre de usuario
            username = self.driver.find_element(By.CLASS_NAME, "new").text
            print("Usuario iniciado sesión:", username)
            return username, self.driver
        except Exception as e:
            print(f"Error en login : {e}")
