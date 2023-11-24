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


class TestCompraVeiculo():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_compraVeiculo(self):
        self.driver.get("https://luizhenrique.pythonanywhere.com/home")
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.set_window_size(1382, 784)
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.LINK_TEXT, "Carros").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.LINK_TEXT, "Motos").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.LINK_TEXT, "Utilitários").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.find_element(By.CSS_SELECTOR, ".navbar-brand").click()
        time.sleep(3)  # Adiciona uma pausa de 3 segundos

        self.driver.close()