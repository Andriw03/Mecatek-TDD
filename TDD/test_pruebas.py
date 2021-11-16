#libreria
import unittest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
#importamos el archivo json con los usuarios
with open('login.json') as file:
    data = json.load(file)

class Test_Mecatek(unittest.TestCase):

        # inicializamos la prueba con chrome
    def setUp(self):
        self.driver = webdriver.Chrome()

        #Ejecutamos la prueba para iniciar sesion   
    def test_login_logout(self,user, passw):
        self.driver.refresh()
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(801, 835)
        #sleep(2)
        self.driver.find_element_by_id('btn_iniciosesion').click()
        #sleep(3)
        self.driver.find_element(By.ID, "id_username").send_keys(user)
        self.driver.find_element(By.ID, "id_password").send_keys(passw)
        #sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        #sleep(3)
        self.driver.find_element_by_id('btn_cerrar_sesion').click()
        #sleep(3)
        self.driver.refresh()
        self.driver.delete_all_cookies()
        self.driver.quit()
        self.driver.close()
    

    def ejecutar_login(self):
        for client in data['user']:
            self.test_login_logout(client['username'],client['password'])
            
'''
    def test_crear_proveedor(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(801, 835)
        sleep(2)
        self.driver.find_element_by_id('btn_registro_pro').click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".col-xs-3").click()
        self.driver.find_element(By.ID, "inputEmail4").click()
        self.driver.find_element(By.ID, "inputEmail4").send_keys("Erika Garrido")
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("erika")
        self.driver.find_element(By.NAME, "Rut").click()
        self.driver.find_element(By.NAME, "Rut").send_keys("92345676-3")
        self.driver.find_element(By.NAME, "correo").click()
        self.driver.find_element(By.NAME, "correo").send_keys("erik@gmail.com")
        self.driver.find_element(By.ID, "inputPassword4").click()
        self.driver.find_element(By.ID, "inputPassword4").send_keys("12345678")
        self.driver.find_element(By.ID, "inputCity").click()
        self.driver.find_element(By.ID, "inputCity").send_keys("987564738")
        self.driver.find_element(By.ID, "inputAddress2").click()
        self.driver.find_element(By.ID, "inputAddress2").send_keys("av alemania")
        sleep(3)
        self.driver.find_element_by_id('btn_registrar_p').click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
        sleep(3)
        self.driver.quit()
    
    def test_crear_provedor_sin_telefono(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(801, 835)
        sleep(2)
        self.driver.find_element_by_id('btn_registro_pro').click()
        sleep(3)
        self.driver.find_element(By.ID, "inputEmail4").click()
        self.driver.find_element(By.ID, "inputEmail4").send_keys("Jasson Aros")
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("jason")
        self.driver.find_element(By.NAME, "Rut").click()
        self.driver.find_element(By.NAME, "Rut").send_keys("21876543-6")
        self.driver.find_element(By.NAME, "correo").click()
        self.driver.find_element(By.NAME, "correo").send_keys("jason@gmail.com")
        self.driver.find_element(By.ID, "inputPassword4").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.find_element(By.ID, "inputPassword4").send_keys("nohomo12")
        self.driver.find_element(By.ID, "inputAddress2").click()
        self.driver.find_element(By.ID, "inputAddress2").send_keys("mercurio 203")
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
        sleep(3)
        self.driver.quit()
    
    def test_crear_cliente(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(801, 835)
        #sleep(2)
        self.driver.find_element_by_id('btn_registro_cli').click()
        #sleep(3)
        self.driver.find_element(By.ID, "inputEmail4").click()
        self.driver.find_element(By.ID, "inputEmail4").send_keys("user09")
        self.driver.find_element(By.CSS_SELECTOR, ".d-grid:nth-child(6) > .form-label").click()
        self.driver.find_element(By.ID, "inputAddress").click()
        self.driver.find_element(By.ID, "inputAddress").send_keys("user09")
        self.driver.find_element(By.NAME, "Rut").click()
        self.driver.find_element(By.NAME, "Rut").send_keys("20529201-2")
        self.driver.find_element(By.NAME, "comuna").click()
        self.driver.find_element(By.NAME, "comuna").send_keys("Quillota")
        self.driver.find_element(By.ID, "inputPassword4").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row > .row").click()
        self.driver.find_element(By.ID, "inputPassword4").click()
        self.driver.find_element(By.ID, "inputPassword4").click()
        self.driver.find_element(By.ID, "inputPassword4").send_keys("user09")
        self.driver.find_element(By.NAME, "correo").click()
        self.driver.find_element(By.NAME, "correo").send_keys("sebastian935@gmail.com")
        self.driver.find_element(By.ID, "inputCity").click()
        self.driver.find_element(By.ID, "inputCity").send_keys("985973994")
        self.driver.find_element(By.ID, "inputAddress2").click()
        self.driver.find_element(By.ID, "inputAddress2").send_keys("Bulnes 1305")
        #sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
        #sleep(5)
        self.driver.quit()

    def test_crear_cliente_sin_rut(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(801, 835)
        sleep(2)
        self.driver.find_element_by_id('btn_registro_cli').click()
        sleep(3)
        self.driver.find_element(By.ID, "inputEmail4").click()
        self.driver.find_element(By.ID, "inputEmail4").send_keys("Estefania Reyes")
        self.driver.find_element(By.ID, "inputAddress").click()
        self.driver.find_element(By.ID, "inputAddress").send_keys("estefla")
        self.driver.find_element(By.NAME, "correo").send_keys("epaureyesf@gmail.com")
        self.driver.find_element(By.ID, "inputPassword4").send_keys("periface")
        self.driver.find_element(By.ID, "inputCity").click()
        self.driver.find_element(By.ID, "inputCity").send_keys("930298981")
        self.driver.find_element(By.NAME, "comuna").click()
        self.driver.find_element(By.NAME, "comuna").send_keys("Valparaiso")
        self.driver.find_element(By.ID, "inputAddress2").click()
        self.driver.find_element(By.ID, "inputAddress2").send_keys("av alemania")
        self.driver.find_element(By.CSS_SELECTOR, ".d-grid:nth-child(12)").click()
        self.driver.find_element(By.NAME, "Rut").click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".d-grid:nth-child(12)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()
        sleep(3)
'''
