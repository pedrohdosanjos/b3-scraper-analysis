from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


from logging_service import setup_logger
from utils import close_ad_if_exists


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

logger.info("_____________________________________")

# wait for table elements
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            '//*[@id="ticker-datagrid-table-content"]/tr[14]',
        )
    )
)

logger.info("Table loaded")

# current table data
table = driver.find_element(By.ID, "ticker-datagrid-table-content")
html_prev = table.get_attribute("innerHTML")

volume = driver.find_element(By.ID, "Volume")
baixas = driver.find_element(By.ID, "Low")

if "selected" in baixas.get_attribute("class") or "selected" in volume.get_attribute(
    "class"
):
    # click on "Altas" button
    altas = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "#High",
            )
        )
    )

    # close ad
    close_ad_if_exists(driver, logger)
    driver.execute_script("arguments[0].scrollIntoView({block :'center'});", altas)
    driver.execute_script("arguments[0].click();", altas)

    logger.info("Clicked on 'Altas' button")

    # wait for button "altas" to be selected
    WebDriverWait(driver, 10).until(
        lambda d: "selected" in d.find_element(By.ID, "High").get_attribute("class")
    )

    logger.info("Button 'Altas' selected")

    # wait for content change
    WebDriverWait(driver, 15).until(
        lambda d: d.find_element(By.ID, "ticker-datagrid-table-content").get_attribute(
            "innerHTML"
        )
        != html_prev
    )

    logger.info("Content changed")

    # wait for table elements
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                '//*[@id="ticker-datagrid-table-content"]/tr[14]',
            )
        )
    )

    logger.info("Table elements visible")

driver.execute_script("arguments[0].scrollIntoView();", altas)

linhas = driver.find_elements(By.CSS_SELECTOR, "#ticker-datagrid-table-content tr")

logger.info(f"Found {len(linhas)} rows")

dados = []
for linha in linhas:
    try:
        ticker = linha.find_element(By.CSS_SELECTOR, "a").text.strip()

        nome = linha.find_element(By.CSS_SELECTOR, ".ds-uitext-xs").text.strip()

        preco = (
            linha.find_element(By.CSS_SELECTOR, ".ds-uitext-number")
            .text.strip()
            .split(" ")[1]
            .replace(",", ".")
        )

        var = (
            linha.find_element(By.CSS_SELECTOR, ".text-trade")
            .text.strip()
            .replace("%", "")
            .replace(",", ".")
        )
        logger.info(f"{ticker} - {nome} - {preco} - {var}")

        dados.append(f"{ticker},{nome},{preco},{var}")
    except:
        continue

with open("cotacoes.txt", "w") as f:
    for item in dados:
        f.write(item + "\n")

logger.info("_____________________________________")

driver.quit()
