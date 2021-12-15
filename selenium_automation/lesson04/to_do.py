import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from smart_assertions import soft_assert, verify_expectations

first_index = 1
second_index = 2
expected_text = "Hello World"
expected_scrolled_text = "This Element is Shown When Scrolled"


class Test_To_Do:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_actions.html")
        driver.implicitly_wait(10)
        global action
        action = ActionChains(driver)

    def teardown_class(cls):
        driver.quit()

    def attach_file(self, name):
        image = "./screen-shots/" + name + ".png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Draggable")
    @allure.description("This test Verify the action- draggable")
    def test_verify_draggable(self):
        dropped = self.get_dropped()
        assert dropped.is_displayed

    @allure.title("Verify Click And hold")
    @allure.description("This test Verify the action- click and hold")
    def test_verify_click_and_hold(self):
        list = self.get_click_and_hold_list(first_index, second_index)
        soft_assert(list[first_index].get_attribute("class") == "ui-widget-content ui-selectee ui-selected")
        soft_assert(list[second_index].get_attribute("class") == "ui-widget-content ui-selectee ui-selected")
        verify_expectations()

    @allure.title("Verify Double Click")
    @allure.description("This test Verify the action- double click")
    def test_verify_double_click(self):
        paragraph = self.get_paragraph_after_double_click()
        assert paragraph == expected_text

    @allure.title("Verify Mouse Movement")
    @allure.description("This test Verify the action- mouse movement")
    def test_verify_mouse_movement(self):
        position = self.move_to_position()
        bg_color = "background-color: rgb(255, 255, 0);"
        assert position.get_attribute("style") == bg_color

    @allure.title("Verify Scrolling")
    @allure.description("This test Verify page scrolling")
    def test_verify_scrolling(self):
        scrolled_text = self.get_text_after_scrolling()
        assert scrolled_text == expected_scrolled_text

    @allure.step("Drag And Drop")
    def get_dropped(self):
        draggable = driver.find_element(By.ID, "draggable")
        droppable = driver.find_element(By.ID, "droppable")
        action.drag_and_drop(draggable, droppable).perform()
        dropped = droppable.find_element(By.TAG_NAME, "p")
        return dropped

    @allure.step("Click And Hold")
    def get_click_and_hold_list(self, l1, l2):
        list = driver.find_elements(By.XPATH, "//ol[@id='select_items']/li")
        action.click_and_hold(list[l1]).click(list[l2]).perform()
        time.sleep(3)
        return list

    @allure.step("Double Click")
    def get_paragraph_after_double_click(self):
        element_to_click = driver.find_element(By.XPATH, "//p[@id='dbl_click']")
        action.double_click(element_to_click).perform()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id='demo']"), "Hello World"))
        paragraph = driver.find_element(By.XPATH, "//p[@id='demo']").text
        return paragraph

    @allure.step("Mouse Movement")
    def move_to_position(self):
        position = driver.find_element(By.XPATH, "//span[@id='mouse_hover']")
        action.move_to_element(position).perform()
        time.sleep(1)
        return position

    @allure.step("Scrolling")
    def get_text_after_scrolling(self):
        script = "window.scrollTo(0, 1000);"
        driver.execute_script(script)
        scrolled_text = driver.find_element(By.XPATH, "//p[@id='scrolled_element']").text
        return scrolled_text
