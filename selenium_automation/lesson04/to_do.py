import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from smart_assertions import soft_assert, verify_expectations

# Question to ask in teacher: call self method in before class

tasks = ["SaedToDo1", "SaedToDo2", "SaedToDo3"]


class Test_To_Do:
    def setup_class(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://todomvc.com/examples/react/#/")
        driver.implicitly_wait(10)
        global action
        action = ActionChains(driver)

    def teardown_class(cls):
        driver.quit()

    def attach_file(self, name):
        image = "./screen-shots/" + name + ".png"  # need to create folder: screen-shots first
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    @allure.title("Verify Create Tasks")
    @allure.description("This test verify Todo Operation:Create Task")
    def test_verify_create_task(self):
        try:
            self.create_tasks_for_testing(tasks)
            self.soft_assert_tasks_creation(tasks)
            verify_expectations()
        except AssertionError as e:
            self.attach_file("test_verify_todo")
            pytest.fail("Test Failed...see details:", e)

    @allure.title("Verify Rename Task")
    @allure.description("This test verify Todo Operation:Rename Task")
    def test_verify_rename_task(self):
        self.rename_task("SaedToDo1", "SaedToDo1Renamed")
        assert self.is_exist("SaedToDo1Renamed")

    @allure.title("Verify Delete Task")
    @allure.description("This test verify Todo Operation:Delete Task")
    def test_verify_delete_task(self):
        self.delete_task("SaedToDo2")
        assert not self.is_exist("SaedToDo2")

    @allure.title("Mark Task")
    @allure.description("This test verify Todo Operation:Mark Task")
    def test_verify_mark_task(self):
        assert self.mark_task("SaedToDo1Renamed")

    @allure.title("Filter Task")
    @allure.description("This test verify Todo Operation:Filter Task")
    def test_verify_filter(self):
        soft_assert(self.filter("Active").get_attribute("class") == "selected")
        soft_assert(self.filter("All").get_attribute("class") == "selected")
        soft_assert(self.filter("Completed").get_attribute("class") == "selected")
        verify_expectations()

    @allure.title("Remote All Completed")
    @allure.description("This test verify Todo Operation:Remove All Completed")
    def test_verify_all_completed(self):
        assert (not self.remove_all_completed())

    @allure.step("Generate a List of tasks for testing,takes a list as an input")
    def create_tasks_for_testing(self, tasks_list):
        for task in tasks_list:
            self.create_task(task)

    @allure.step("Soft assert task creation")
    def soft_assert_tasks_creation(self, tasks):
        for task in tasks:
            soft_assert(self.is_exist(task))

    @allure.step("Create a new task")
    def create_task(self, task):
        input = driver.find_element(By.XPATH, ("//input[@class='new-todo']"))
        action.send_keys(task).click(input).send_keys(Keys.RETURN).perform()

    @allure.step("Check if a task exists")
    def is_exist(self, task):
        size = len(driver.find_elements(By.XPATH, "//label[text()='" + task + "']"))
        if (size > 0):
            return True
        return False

    @allure.step("Rename a Task by providing the old and new name")
    def rename_task(self, old_name, new_name):
        current = driver.find_element(By.XPATH, "//label[text()='" + old_name + "']")
        action.click(current).double_click().send_keys(new_name).send_keys(Keys.ENTER).perform()

    @allure.step("Delete a given task")
    def delete_task(self, task):
        label = driver.find_element(By.XPATH, "//label[text()='" + task + "']")
        action.move_to_element(label).click().double_click()
        action.send_keys(Keys.BACK_SPACE).send_keys(Keys.ENTER)
        action.perform()

    @allure.step("Mark Task as completed")
    def mark_task(self, task):
        parent_div = driver.find_element(By.XPATH, "//label[text()='" + task + "']/..")
        toggle = parent_div.find_element(By.XPATH, "//input[@class='toggle']")
        action.click(toggle).perform()
        return toggle

    @allure.step("Filter Task By Type")
    def filter(self, type):
        selected_type = driver.find_element(By.PARTIAL_LINK_TEXT, type)
        selected_type.click()
        time.sleep(1)
        return selected_type

    @allure.step("Remove all completed Tasks")
    def remove_all_completed(self):
        driver.find_element(By.XPATH, "//button[@class='clear-completed']").click()
        status = len(driver.find_elements(By.XPATH, "//span[@class='todo-count']/strong")) == 0
        print("STATUS:" + str(status))
        return status
