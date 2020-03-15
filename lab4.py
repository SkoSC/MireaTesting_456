from selenium import webdriver
import unittest
from ddt import ddt, data, unpack


@ddt
class ArtlebedevCaseTest(unittest.TestCase):
    driver = webdriver.Firefox(executable_path=r"C:\Program Files\geckodriver.exe")

    def setUp(self):
        self.driver.get("https://www.artlebedev.ru/case/")
        self.driver.execute_script("window.scrollTo(0, 1000)")

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
        {"source": "TEST", "target": "TEST"})
    @unpack
    def test_upper_case(self, source, target):
        self._select_mode("ВЕРХНИЙ РЕГИСТР")
        self._capture_source().clear()
        if (len(source) != 0):
            self._capture_source().send_keys(source)
        self.driver.implicitly_wait(2)
        self.assertEqual(target, self._capture_target().get_attribute("value"))

    @data(
        {"source": "hello world", "target": "hello world"},
        {"source": "TEST", "target": "test"})
    @unpack
    def test_lower_case(self, source, target):
        self._select_mode("нижний регистр")
        self._capture_source().clear()
        if (len(source) != 0):
            self._capture_source().send_keys(source)
        self.driver.implicitly_wait(2)
        self.assertEqual(target, self._capture_target().get_attribute("value"))

    @data(
        {"source": "hello world", "target": "Hello World"},
        {"source": "TEST", "target": "Test"})
    @unpack
    def test_captialize(self, source, target):
        self._select_mode("Заглавные Буквы")
        self._capture_source().clear()
        if (len(source) != 0):
            self._capture_source().send_keys(source)
        self.driver.implicitly_wait(2)
        self.assertEqual(target, self._capture_target().get_attribute("value"))

    @data(
        {"source": "hello world", "target": "Hello world"},
        {"source": "TEST", "target": "Test"})
    @unpack
    def test_captialize_first(self, source, target):
        self._select_mode("Первая заглавная")
        self._capture_source().clear()
        if (len(source) != 0):
            self._capture_source().send_keys(source)
        self.driver.implicitly_wait(2)
        self.assertEqual(target, self._capture_target().get_attribute("value"))

    @data(
        {"source": "Hello World", "target": "hELLO wORLD"},
        {"source": "TEST", "target": "test"})
    @unpack
    def test_invert(self, source, target):
        self._select_mode("иНВЕРСИЯ рЕГИСТРА")
        self._capture_source().clear()
        if (len(source) != 0):
            self._capture_source().send_keys(source)
        self.driver.implicitly_wait(2)
        self.assertEqual(target, self._capture_target().get_attribute("value"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
