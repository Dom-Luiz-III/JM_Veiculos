# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAddcarro():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_addcarro(self):
        self.driver.get("https://luizhenrique.pythonanywhere.com/")
        self.driver.set_window_size(945, 1032)

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, ".titulo:nth-child(1)").click()

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("luiz")

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("luiz")

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, ".model-carro .addlink").click()

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_modelo").click()
        self.driver.find_element(By.ID, "id_modelo").send_keys("ford")

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_marca").click()
        self.driver.find_element(By.ID, "id_marca").send_keys("mustang")

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_ano_fabricacao").click()
        self.driver.find_element(By.ID, "id_ano_fabricacao").send_keys("2023")

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_estado").click()
        dropdown = self.driver.find_element(By.ID, "id_estado")
        dropdown.find_element(By.XPATH, "//option[. = 'Novo']").click()

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_km_rodados").click()
        self.driver.find_element(By.ID, "id_km_rodados").send_keys("20000")

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_formas_pagamento").click()
        dropdown = self.driver.find_element(By.ID, "id_formas_pagamento")
        dropdown.find_element(By.XPATH, "//option[. = 'A Vista']").click()

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_situacao").click()
        dropdown = self.driver.find_element(By.ID, "id_situacao")
        dropdown.find_element(By.XPATH, "//option[. = 'A Venda']").click()

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.ID, "id_placa").click()
        self.driver.find_element(By.ID, "id_placa").send_keys("BHT3A29")

        time.sleep(3)  # Atraso de 3 segundos

        self.driver.find_element(By.NAME, "_save").click()