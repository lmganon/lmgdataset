import logging
from time import sleep

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class GptScraper:
    def __init__(self) -> None:
        self.driver = uc.Chrome(version_main=113)
        self.wait = WebDriverWait(self.driver, 10)

    def __del__(self) -> None:
        self.driver.quit()

    def click_element(self, by: By, identifier: str) -> None:
        sleep(2)
        element: WebElement = self.wait.until(
            EC.visibility_of_element_located((by, identifier))
        )
        element.click()
        sleep(2)

    def send_keys_element(self, by: By, identifier: str, keys: str) -> None:
        sleep(2)
        element: WebElement = self.wait.until(
            EC.visibility_of_element_located((by, identifier))
        )
        element.send_keys(keys + Keys.ENTER)
        sleep(2)

    def get_openai(self) -> None:
        self.driver.get("https://chat.openai.com/")
        self.click_element(By.XPATH, '//button/div[text()="Log in"]')

    def log_in_google(self, user: str, password: str) -> None:
        self.click_element(By.XPATH, '//button/span[text()="Continue with Google"]')
        self.send_keys_element(By.XPATH, '//input[@id="identifierId"]', user)
        self.send_keys_element(By.XPATH, '//input[@type="password"]', password)

    def click_new_chat(self) -> None:
        self.click_element(By.XPATH, '//a[text()="New chat"]')

    def select_gpt_4(self) -> None:
        self.click_element(By.XPATH, '//span[text()="GPT-4"]')

    def send_prompt(self, promt: str) -> str:
        scraper.send_keys_element(By.XPATH, "//textarea[@id='prompt-textarea']", promt)
        sleep(5)
        response: WebElement = scraper.driver.find_element(
            By.XPATH,
            (
                "//*[local-name() = 'svg']/*[local-name() = 'title' and text() = 'ChatGPT']"
                "/ancestor::div[4]//p"
            ),
        )
        return response.text


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the scraper...")
    scraper = GptScraper()
    scraper.get_openai()
    scraper.log_in_google()
    logging.info("Scraper started successfully.")
    scraper.click_new_chat()
    scraper.select_gpt_4()
    response = scraper.send_prompt("hey this is a test")
    logging.info(f"The response was {response}.")
