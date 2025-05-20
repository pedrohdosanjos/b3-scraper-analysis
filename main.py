from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from logging_service import setup_logger


URL = "https://www.infomoney.com.br/cotacoes/b3/acao"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.set_window_size(1280, 800)

driver.set_window_position(-1280, 0)

logger = setup_logger("logger", "scraper.log")

driver.get(URL)

# click in "Altas" button
altas = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "#High",
        )
    )
)
driver.execute_script("arguments[0].scrollIntoView({block :'center'});", altas)
driver.execute_script("arguments[0].click();", altas)

logger.info("Clicked on 'Altas' button")

# wait for button "altas" to be selected
WebDriverWait(driver, 10).until(
    lambda d: "selected" in d.find_element(By.ID, "High").get_attribute("class")
)

logger.info("Button 'Altas' selected")

sleep(2)

# wait for table elements
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            '//*[@id="ticker-datagrid-table-content"]/tr[14]',
        )
    )
)

logger.info("Table found")

driver.execute_script("arguments[0].scrollIntoView();", altas)

linhas = driver.find_elements(By.CSS_SELECTOR, "#ticker-datagrid-table-content tr")

logger.info(f"Found {len(linhas)} rows")
logger.info(f"")

dados = []
for linha in linhas:
    try:
        ticker = linha.find_element(By.CSS_SELECTOR, "a").text.strip()
        logger.info(f"Ticker: {ticker}")

        nome = linha.find_element(By.CSS_SELECTOR, ".ds-uitext-xs").text.strip()
        logger.info(f"Nome: {nome}")

        preco = (
            linha.find_element(By.CSS_SELECTOR, ".ds-uitext-number")
            .text.strip()
            .split(" ")[1]
            .replace(",", ".")
        )
        logger.info(f"Preço: {preco}")

        var = (
            linha.find_element(By.CSS_SELECTOR, ".text-trade")
            .text.strip()
            .replace("%", "")
            .replace(",", ".")
        )
        logger.info(f"Variação: {var}")

        dados.append(f"{ticker},{nome},{preco},{var}")
        logger.info(f"")
    except:
        continue  # pular linhas incompletas

with open("cotacoes.txt", "w") as f:
    for item in dados:
        f.write(item + "\n")


driver.quit()
