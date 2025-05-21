from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


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
