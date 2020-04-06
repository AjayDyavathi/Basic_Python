from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://play2048.co')
time.sleep(3)
grid = browser.find_element_by_tag_name('body')
for x in range(100):
    time.sleep(.1)
    grid.send_keys(Keys.UP)
    time.sleep(.1)
    grid.send_keys(Keys.RIGHT)
    time.sleep(.1)
    grid.send_keys(Keys.DOWN)
    time.sleep(.1)
    grid.send_keys(Keys.LEFT) 