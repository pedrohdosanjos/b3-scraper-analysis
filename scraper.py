from selenium.webdriver.common.by import By

from utils.utils import init_driver, scrape_rows, select_filter, wait_table

URL = "https://www.infomoney.com.br/cotacoes/b3/acao"


def run_scraper(logger):
    driver = init_driver()
    driver.get(URL)
    wait_table(driver)

    resultados = {}
    html_prev = driver.find_element(
        By.ID, "ticker-datagrid-table-content"
    ).get_attribute("innerHTML")

    for filtro in ["High", "Low"]:
        html_prev = select_filter(driver, filtro, logger, html_prev)
        resultados[filtro] = scrape_rows(driver, logger)

    with open("data/cotacoes_altas.txt", "w", encoding="utf-8") as f_altas:
        for linha in resultados["High"]:
            f_altas.write(linha + "\n")
    with open("data/cotacoes_baixas.txt", "w", encoding="utf-8") as f_baixas:
        for linha in resultados["Low"]:
            f_baixas.write(linha + "\n")

    driver.quit()
    logger.info("Scraping concluído para altas e baixas.")
