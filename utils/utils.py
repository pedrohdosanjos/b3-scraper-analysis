from asyncio import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.set_window_size(1280, 800)
    return driver


def wait_table(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="ticker-datagrid-table-content"]/tr[14]')
        )
    )


def select_filter(driver, filter_id, logger, previous_html):
    btn = driver.find_element(By.ID, filter_id)
    if "selected" not in btn.get_attribute("class"):
        close_ad_if_exists(driver, logger)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        driver.execute_script("arguments[0].click();", btn)
        logger.info(f"Clicou em '{filter_id}'")
        WebDriverWait(driver, 10).until(
            lambda d: "selected"
            in d.find_element(By.ID, filter_id).get_attribute("class")
        )
        WebDriverWait(driver, 15).until(
            lambda d: d.find_element(
                By.ID, "ticker-datagrid-table-content"
            ).get_attribute("innerHTML")
            != previous_html
        )
        wait_table(driver)
    return driver.find_element(By.ID, "ticker-datagrid-table-content").get_attribute(
        "innerHTML"
    )


def scrape_rows(driver, logger):
    linhas = driver.find_elements(By.CSS_SELECTOR, "#ticker-datagrid-table-content tr")
    dados = []
    for linha in linhas:
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of(linha))
            ticker = linha.find_element(By.CSS_SELECTOR, "a").text.strip()
            nome = linha.find_element(By.CSS_SELECTOR, ".ds-uitext-xs").text.strip()
            preco = (
                linha.find_element(By.CSS_SELECTOR, ".ds-uitext-number")
                .text.split(" ")[1]
                .replace(",", ".")
            )
            var = (
                linha.find_elements(By.CSS_SELECTOR, ".text-trade")[0]
                .text.replace("%", "")
                .replace(",", ".")
            )
            var12 = (
                linha.find_elements(By.CSS_SELECTOR, ".text-trade")[1]
                .text.replace("%", "")
                .replace(",", ".")
            )
            # clicar para setor
            try:
                link = linha.find_element(By.CSS_SELECTOR, "a")
                driver.execute_script("arguments[0].click();", link)
                clicked = True
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".code-ativo"))
                )
                setor = driver.find_elements(By.TAG_NAME, "h3")[2].text.split(": ")[1]
                clicked = False
                driver.back()
                wait_table(driver)
            except:
                logger.error("Erro ao obter setor")
                setor = "N/A"
                if clicked:
                    driver.back()
                    wait_table(driver)
                    clicked = False
            logger.info(f"{ticker} | {nome} | {preco} | {var} | {var12} | {setor}")
            dados.append(f"{ticker},{nome},{preco},{var},{var12},{setor}")
        except:
            logger.error("Linha inválida")
    return dados


def close_ad_if_exists(driver, logger):
    try:
        # locate iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")

        for iframe in iframes:
            try:
                driver.switch_to.frame(iframe)

                close_btns = driver.find_elements(By.ID, "fechar")
                if close_btns and close_btns[0].is_displayed():
                    driver.execute_script("arguments[0].click();", close_btns[0])
                    logger.info("Fechando propaganda")
                    break

            except Exception:
                pass

            finally:
                driver.switch_to.default_content()

    except NoSuchElementException:
        pass
