from msedge.selenium_tools import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# execute isso no terminal -  python manage.py test core.tests.test_teste1

class TestTeste1():
    def setup_method(self, method):
        # Configura o caminho para o executável do WebDriver do Microsoft Edge
        self.driver = Edge(executable_path=r'C:\Users\vg160\PycharmProjects\Django\JM_Veiculos\core\tests\msedgedriver.exe')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_teste1(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(971, 692)
        element = self.driver.find_element(By.CSS_SELECTOR, "html")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "html")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "html")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "contato-form").click()
        self.driver.find_element(By.ID, "nome").click()
        self.driver.find_element(By.ID, "nome").send_keys("vinicius")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("vini@gomes.com.br")
        self.driver.find_element(By.ID, "telefone").click()
        self.driver.find_element(By.ID, "telefone").send_keys("1234567890")
        self.driver.find_element(By.ID, "mensagem").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "html")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "html")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "html")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "mensagem").send_keys("teste 1 feito!")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(6)").click()
