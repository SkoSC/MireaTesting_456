from selenium import webdriver
import unittest
from ddt import ddt, data, unpack


@ddt
class ArtlebedevCaseTest(unittest.TestCase):
    driver = webdriver.Firefox(r"C:\Program Files\chromedriver.exe")

    def setUp(self):
        self.driver.get("https://www.artlebedev.ru/case/")

    def tearDown(self):
        self.driver.refresh()

    def _select_mode(self, mode):
        self.driver.find_element_by_link_text(mode).click()

    def _capture_source(self):
        return self.driver.find_element_by_id("source")

    def _capture_target(self):
        return self.driver.find_element_by_id("target")

    def test_title(self):
        title_element = self.driver.find_element_by_class_name("als-text-title")
        self.assertEqual("Конвертер регистров", title_element.text)

    def test_method_text(self):
        table = self.driver.find_element_by_id("method-tabs")
        children = table.find_elements_by_xpath(".//*")
        self.assertEqual("ВЕРХНИЙ РЕГИСТР", children[0].text)
        self.assertEqual("нижний регистр", children[1].text)
        self.assertEqual("Заглавные Буквы", children[2].text)
        self.assertEqual("Первая заглавная", children[3].text)
        self.assertEqual("иНВЕРСИЯ рЕГИСТРА", children[4].text)

    @data(
        {"source": "hello world", "target": "HELLO WORLD"},
        {"source": "", "target": ""},
        {"source": "TEST", "target": "TEST"})
    @unpack
    def test_upper_case(self, source, target):
        self._select_mode("ВЕРХНИЙ РЕГИСТР")
        self._capture_source().send_keys(source)
        self.driver.implicitly_wait(1)
        print(self._capture_target().text)
        self.assertEqual(target, self._capture_target().text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
