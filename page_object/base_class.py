from typing import Tuple

from selenium.common import MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    def _open_page(self, page_url):
        self.driver.get(page_url)

    def get_elements(self, locator: Tuple[str, str]):
        return self.driver.find_elements(locator[0], locator[1])

    def _click_element(self, locator: Tuple[str, str]):
        self.driver.find_element(locator[0], locator[1]).click()

    def _send_keys(self, locator: Tuple[str, str], value: str):
        self.driver.find_element(locator[0], locator[1]).send_keys(value)

    def _get_element_text(self, locator: Tuple[str, str]):
        return self.driver.find_element(locator[0], locator[1]).text

    def _get_element_text_and_wait(self, locator: Tuple[str, str], wait_time: int = 10):
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def _get_element_attribute(self, locator: Tuple[str, str], attribute_name: str):
        return self.driver.find_element(locator[0], locator[1]).get_attribute(attribute_name)

    def _check_element_visibility_and_wait(self, locator: Tuple[str, str], wait_time: int = 10):
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(EC.visibility_of_element_located(locator))

        return element

    def _is_element_displayed(self, locator: Tuple[str, str]):
        return self.driver.find_element(locator[0], locator[1]).is_displayed()

    def _click_element_and_wait(self, locator: Tuple[str, str], wait_time: int = 20):
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.invisibility_of_element(locator))
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def _move_to_element(self, locator: Tuple[str, str]):
        element = self.driver.find_element(locator[0], locator[1])
        actions = ActionChains(self.driver)
        try:
            actions.move_to_element(element).perform()
        except MoveTargetOutOfBoundsException as error:
            print(error)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def _move_element_and_click(self, locator: Tuple[str, str]):
        element = self.driver.find_element(locator[0], locator[1])
        actions = ActionChains(self.driver)
        try:
            actions.move_to_element(element).click().perform()
        except MoveTargetOutOfBoundsException as error:
            print(error)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def switch_to_window(self, window_handles_index: int):
        self.driver.switch_to.window(self.driver.window_handles[window_handles_index])

    def check_open_page(self, url: str):
        wait = WebDriverWait(self.driver, 50)
        assert wait.until(EC.url_contains(url))
