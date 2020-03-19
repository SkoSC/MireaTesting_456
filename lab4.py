from time import sleep

from selenium import webdriver
from random import shuffle

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"C:\Program Files\geckodriver.exe")

with open("site-comfig.txt", "r") as file:
    urls = [line.replace('\n', '') for line in file.readlines()]

shuffle(urls)

with open("site-comfig.txt", "w") as file:
    file.write("\n".join(urls))

for i, url in enumerate(urls):
    driver.execute_script(f'window.open("{url}", "_blank")')
    sleep(2)


for handle in driver.window_handles:
    driver.switch_to.window(handle)
    sleep(2)
    driver.close()