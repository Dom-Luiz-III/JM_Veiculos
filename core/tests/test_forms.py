from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Adiciona o caminho para o diretório contendo o MicrosoftWebDriver.exe
edge_driver_path = r'C:\Windows\msedgedriver'

# Adiciona o caminho ao PATH
# ( ele vai procurar por arquivos executáveis quando você tenta executar um programa a partir do terminal ou prompt de comando)
os.environ['PATH'] += ';' + edge_driver_path


# execute isso no terminal -  python manage.py test core.tests.test_forms

driver = webdriver.Edge()

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
    time.sleep(10)

    # Verificar se a mensagem de sucesso está visível
    success_message = driver.find_element(By.ID, "success-message")
    assert "Cadastro Enviado com Sucesso!" in success_message.text

    input("Pressione Enter para fechar a janela do navegador...")

except Exception as e:
    print("O teste de login falhou:", e)

finally:
    driver.quit()
