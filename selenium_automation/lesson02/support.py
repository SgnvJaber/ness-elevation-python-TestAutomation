from selenium.webdriver.common.by import By

expected = "elem "


class Support:
    def verify_elements(self, driver):
        elements = driver.find_elements(By.XPATH, "//div[@id='ms-aloha']/div/ul/li[@class='ms-elem-selectable']")
        start_index = 2
        for elem in elements:
            start_index += 1
            expected_output = expected + str(start_index)
            assert elem.text == expected_output
