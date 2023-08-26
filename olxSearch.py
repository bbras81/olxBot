from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.olx.pt/")
sleep(3)

menssage = 'honda nc750x'

button_1 = driver.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]')
button_1.click()

sleep(3)

search = driver.find_element('xpath', '//*[@id="headerSearch"]')
search.send_keys(menssage + Keys.RETURN)
sleep(3)

items = driver.find_elements('xpath', '//*[@data-cy="l-card"]')
print(len(items))
print(items[0].text)

driver.quit()
