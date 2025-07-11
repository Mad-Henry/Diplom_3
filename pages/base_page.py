import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from URLs import BASE_URL


class BasePage:
        

        def __init__(self, browser, timeout=15):
            self.browser = browser
            self.wait = WebDriverWait(browser, timeout)
            self.browser_name = self.browser.capabilities["browserName"].lower()


        def open(self, url_suffix):
            self.browser.get(BASE_URL + url_suffix)


        def current_url(self):
            return self.browser.current_url
        

        def save_current_tab(self):
            return self.browser.current_window_handle    


        def list_of_tabs(self):
            return self.browser.window_handles
        

        def switch_to_tab(self, tab_num):
            self.browser.switch_to.window(tab_num)        


        def wait_for_blank_page(self):
            self.wait.until(lambda d: d.current_url != "about:blank")

        
        def wait_until_clickable(self, locator):
            return self.wait.until(expected_conditions.element_to_be_clickable(locator))
        

        def click(self, locator):
            self.wait_until_clickable(locator).click()


        def forse_click(self, locator):
            element = self.find(locator)
            self.browser.execute_script("arguments[0].click();", element)


        def send_keys(self, locator, keys):
            self.wait_until_clickable(locator).send_keys(keys)

        
        def find(self, locator):
            return self.browser.find_element(*locator)
              

        def scroll_to_element(self, locator):
            element = self.find(locator)
            self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)    


        def wait_until_stale(self, element):
            self.wait.until(expected_conditions.staleness_of(element))


        def wait_for_invisibility(self, locator):
            return self.wait.until(expected_conditions.invisibility_of_element_located(locator))


        def wait_for_presence(self, locator):
            return self.wait.until(expected_conditions.presence_of_element_located(locator))


        def present_of_element(self, locator):
            try:
                self.wait_for_presence(locator)
            except NoSuchElementException:
                return False
            return True
        
        
        @allure.step("Клик по элементу в Firefox")
        def click_on_element(self, locator):
            target = self.wait_for_visible(locator)
            click = ActionChains(self.browser)
            click.move_to_element(target).click().perform()


        @allure.step("Проверка отображения элемента")
        def check_elements_displaying(self, locator):
            return self.browser.find_element(*locator).is_displayed()
            

        @allure.step("Перетаскивание элемента на странице")
        def drag_and_drop_element(self, source_element, target_element):
            script = """
                function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                    var dataTransfer = new DataTransfer();
                    var dragStartEvent = new DragEvent('dragstart', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragStartEvent);

                    var dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    destinationNode.dispatchEvent(dropEvent);
                    var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
            self.browser.execute_script(script, source_element, target_element)
