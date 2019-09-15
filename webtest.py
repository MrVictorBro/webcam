from selenium import webdriver
import time

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("no-sandbox")
options.add_argument("window-size=800,800")
options.add_argument("allow-file-access-from-files")
#options.add_argument("use-fake-device-for-media-stream")
options.add_argument("use-fake-ui-for-media-stream")

driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
driver.get('https://10.219.144.39/videoroomtest.html')
# time.sleep(5)
driver.implicitly_wait(10)
driver.find_element_by_id("start").click()
driver.find_element_by_id("username").send_keys("qq1")
driver.find_element_by_id("register").click()
time.sleep(10)
driver.find_element_by_id("start").click()
time.sleep(2)
driver.quit()
