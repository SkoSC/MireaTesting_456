import json
import unittest
from time import sleep

from selenium import webdriver


class Program:
    def find_latest_messages(self):
        with open("credentials.json", "r") as file:
            creds = json.loads(file.read())

        driver = webdriver.Firefox(executable_path=r"C:\Program Files\geckodriver.exe")
        driver.get("https://vk.com")

        def vk_login_selenium(browser, settings):
            browser.get('https://www.vk.com')

            email = browser.find_element_by_id('index_email')
            email.click()
            email.clear()
            email.send_keys(settings['email'])

            password = browser.find_element_by_id('index_pass')
            password.click()
            password.clear()
            password.send_keys(settings['password'])

            login = browser.find_element_by_id('index_login_button')
            login.click()

        vk_login_selenium(driver, creds)
        sleep(10)
        driver.find_element_by_xpath("//a[@href='/im']").click()
        sleep(10)
        driver.find_element_by_xpath("//*[contains(text(), 'TEST')]").click()
        return list(map(lambda x: x.text, driver.find_elements_by_class_name("im-mess--text")[-10:]))

class Test(unittest.TestCase):

    def test(self):
        actual = Program().find_latest_messages()
        self.assertEqual(
            ["message 2", "message 3", "message 4", "message 5", "message 6", "message 7", "message 8", "message 9", "message 10", "Алексей Яковлев пригласил Олега Лобанова"],
            actual
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)