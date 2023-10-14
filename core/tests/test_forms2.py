from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

form_url = "http://127.0.0.1:8000/"

try:
    driver.get(form_url)

    user_nome = driver.find_element(By.ID, "nome")
    user_email = driver.find_element(By.ID, "email")
    user_tell = driver.find_element(By.ID, "telefone")
    user_mensagem = driver.find_element(By.ID, "mensagem")
    user_botao = driver.find_element(By.ID, "button")

    user_nome.send_keys("vinicius")
    time.sleep(3)  # Pausa por 3 segundos
    user_email.send_keys("vinicius@gomes.com.br")
    time.sleep(3)  # Pausa por 3 segundos
    user_tell.send_keys("999999-999999")
    time.sleep(3)  # Pausa por 3 segundos
    user_mensagem.send_keys("teste simples concluído")
    time.sleep(3)  # Pausa por 3 segundos
    user_botao.click()
    time.sleep(10)

    # Verificar se a mensagem de sucesso está visível
    success_message = driver.find_element(By.ID, "success-message")
    assert "Cadastro Enviado com Sucesso!" in success_message.text

    input("Pressione Enter para fechar a janela do navegador...")

except Exception as e:
    print("O teste de login falhou:", e)

finally:
    driver.quit()
