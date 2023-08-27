from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd



driver = webdriver.Chrome()

driver.get("https://www.olx.pt/")
sleep(1)
button_1 = driver.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]')
button_1.click()

sleep(3)

menssage = 'honda nc750x'
search = driver.find_element('xpath', '//*[@id="headerSearch"]')
search.send_keys(menssage + Keys.RETURN)


driver.find_element('xpath', '//*[@id="mainContent"]/div[2]/form/div[3]/div[4]/div/div/div[1]/div/div').click()
driver.find_element('xpath', '//*[@id="mainContent"]/div[2]/form/div[3]/div[4]/div/div/div[1]/div/div/div[2]/div[2]/div[3]').click()

sleep(8)


items = driver.find_elements('xpath', '//*[@data-cy="l-card"]')
#print(len(items))
dividir = []
dataBase = []
for i in range(len(items)):
    dividir.append(items[i].text.split('\n'))
    
    print(dividir)
    print(len(dividir))
    
    
    

    oneItem = {}
    match len(dividir[i][0]):
    
    
    case 4:
        oneItem['top'] = None
        oneItem['name'] = dividir[i][0]
        oneItem["price"] = dividir[i][1]
        oneItem["neg"] = None
        oneItem['local data'] = dividir[i][2]
        oneItem["year km"] = dividir[i][3]
        dataBase.append(oneItem)
    case 5:
        if 'TOP' in dividir[0]:
            oneItem['top'] = dividir[i][0]
            oneItem['name'] = dividir[i][1]
            oneItem["price"] = dividir[i][2]
            oneItem["neg"] = None
            oneItem['local data'] = dividir[i][3]
            oneItem["year km"] = dividir[i][4]
            dataBase.append(oneItem)
        else:
            oneItem['top'] = None
            oneItem['name'] = dividir[i][0]
            oneItem["price"] = dividir[i][1]
            oneItem["neg"] = dividir[i][2]
            oneItem['local data'] = dividir[i][3]
            oneItem["year km"] = dividir[i][4]
            dataBase.append(oneItem)
    case 6:
        oneItem['top'] = dividir[i][0]
        oneItem['name'] = dividir[i][1]
        oneItem["price"] = dividir[i][2]
        oneItem["neg"] = dividir[i][3]
        oneItem['local data'] = dividir[i][4]
        oneItem["year km"] = dividir[i][5]
        dataBase.append(oneItem)
    #
    # dividir = []

#print(items[1].text)
print(dataBase)



#pd.DataFrame(dataBase)

driver.quit()