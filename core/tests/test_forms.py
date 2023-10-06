from msedge.selenium_tools import Edge, EdgeOptions

# Configura o tempo limite para 10 segundos
edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.page_load_strategy = 'eager'  # Adicione esta linha para definir a estratégia de carregamento de página

# Defina o tempo limite de conexão em segundos
timeout = 10  # Você pode ajustar este valor conforme necessário

# Inicialize o driver do Microsoft Edge
driver = Edge(executable_path=r'C:\Users\vg160\OneDrive\Área de Trabalho\msedgedriver.exe', options=edge_options)

driver.set_page_load_timeout(timeout)  # Define o tempo limite de carregamento de página

driver.get('http://127.0.0.1:8000/')
assert "JM Veiculos" in driver.title

nome_input = driver.find_element_by_id('nome')
email_input = driver.find_element_by_id('email')
telefone_input = driver.find_element_by_id('telefone')
mensagem_input = driver.find_element_by_id('mensagem')
# como existem duas classes do botão com o mesmo nome, exige um outro tipo de comando para localizar o botão
enviar_button = driver.find_element_by_xpath('//form[@id="contato-form"]//button[@class="btn btn-primary"]')

nome_input.send_keys('João da Silva')
email_input.send_keys('joao@example.com')
telefone_input.send_keys('40028922')
mensagem_input.send_keys('Estou interessado neste carro. Por favor, entre em contato comigo.')
enviar_button.click()

# pip install msedge-selenium-tools
