from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time

# execute isso no terminal -  python manage.py test core.tests.test_forms

driver = Edge()

form_url = "http://127.0.0.1:8000/"

try:
    driver.get(form_url)

    user_nome = driver.find_element(By.ID, "nome")
    user_email = driver.find_element(By.ID, "email")
    user_tell = driver.find_element(By.ID, "telefone")
    user_mensagem = driver.find_element(By.ID, "mensagem")
    user_botao = driver.find_element(By.ID, "button")

    user_nome.send_keys("vinicius")
    time.sleep(3)  # Pausa por 3 segundo
    user_email.send_keys("vinicius@gomes.com.br")
    time.sleep(3)  # Pausa por 3 segundo
    user_tell.send_keys("999999-999999")
    time.sleep(3)  # Pausa por 3 segundo
    user_mensagem.send_keys("teste simples concluído")
    time.sleep(3)  # Pausa por 3 segundo
    user_botao.click()

    input("Pressione Enter para fechar a janela do navegador...")

except Exception as e:
    print("O teste de login falhou:", e)

finally:
    driver.quit()
