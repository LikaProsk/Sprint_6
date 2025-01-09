from typing import Tuple

from selenium.common import MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def _open_page(self, driver, page_url):
        driver.get(page_url)

    def get_elements(self, driver, locator: Tuple[str, str]):
        return driver.find_elements(locator[0], locator[1])

    def _click_element(self, driver, locator: Tuple[str, str]):
        driver.find_element(locator[0], locator[1]).click()

    def _send_keys(self, driver, locator: Tuple[str, str], value: str):
        driver.find_element(locator[0], locator[1]).send_keys(value)

    def _get_element_text(self, driver, locator: Tuple[str, str]):
        return driver.find_element(locator[0], locator[1]).text

    def _get_element_text_and_wait(self, driver, locator: Tuple[str, str], wait_time: int = 10):
        wait = WebDriverWait(driver, wait_time)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def _get_element_attribute(self, driver, locator: Tuple[str, str], attribute_name: str):
        return driver.find_element(locator[0], locator[1]).get_attribute(attribute_name)

    def _check_element_visibility_and_wait(self, driver, locator: Tuple[str, str], wait_time: int = 10):
        wait = WebDriverWait(driver, wait_time)
        element = wait.until(EC.visibility_of_element_located(locator))

        return element

    def _is_element_displayed(self, driver, locator: Tuple[str, str]):
        return driver.find_element(locator[0], locator[1]).is_displayed()

    def _click_element_and_wait(self, driver, locator: Tuple[str, str], wait_time: int = 20):
        wait = WebDriverWait(driver, wait_time)
        wait.until(EC.invisibility_of_element(locator))
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def _move_to_element(self, driver, locator: Tuple[str, str]):
        element = driver.find_element(locator[0], locator[1])
        actions = ActionChains(driver)
        try:
            actions.move_to_element(element).perform()
        except MoveTargetOutOfBoundsException as error:
            print(error)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def _move_element_and_click(self, driver, locator: Tuple[str, str]):
        element = driver.find_element(locator[0], locator[1])
        actions = ActionChains(driver)
        try:
            actions.move_to_element(element).click().perform()
        except MoveTargetOutOfBoundsException as error:
            print(error)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            driver.execute_script("arguments[0].click();", element)

    def switch_to_window(self, driver, window_handles_index: int):
        driver.switch_to.window(driver.window_handles[window_handles_index])
