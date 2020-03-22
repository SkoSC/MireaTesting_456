from time import sleep

from ddt import ddt, data
from selenium import webdriver
from random import shuffle, seed
import unittest

class Program:

    driver = webdriver.Firefox(executable_path=r"C:\Program Files\geckodriver.exe")
    urls = []

    def read_urls_from_config(self):
        with open(f"site-config.txt", "r") as file:
            self.urls = [line.replace('\n', '') for line in file.readlines()]

    def shuffle(self):
        shuffle(self.urls)

    def write_urls_to_config(self):
        with open(f"site-config.txt", "w") as file:
            file.write("\n".join(self.urls))

    def open_tabs_from_urls(self):
        for i, url in enumerate(self.urls):
            self.driver.execute_script(f'window.open("{url}", "_blank")')
            sleep(1)

    def close_open_tabs_reversed(self):
        for handle in self.driver.window_handles[1:]:
            self.driver.switch_to.window(handle)
            sleep(1)
            self.driver.close()

class Test(unittest.TestCase):

    def test(self):
        with open("site-config.txt", 'w') as file:
            with open("site-config-setup.txt", "r") as setup:
                file.write(setup.read())

        seed(1)
        program = Program()
        program.read_urls_from_config()

        self.assertEqual(10, len(program.urls))

        program.shuffle()

        program.write_urls_to_config()

        program.open_tabs_from_urls()

        self.assertEqual(11, len(program.driver.window_handles))

        program.close_open_tabs_reversed()

        self.assertEqual(1, len(program.driver.window_handles))

        with open("site-config.txt", "r") as file:
            with open("site-config-expected.txt", "r") as expected:
                self.assertEqual(expected.read(), file.read())

if __name__ == '__main__':
    unittest.main(verbosity=2)