import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


f = open('break_break.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerow(['Id', 'Brand', 'Year', 'Set', 'Description', 'Card Number',
             'Player Name', 'Grade', 'Auto Grade', 'Population', 'Population Higher'])

service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)

for id in range(54000, 55000):
    id_str = str(id).zfill(7)

    row = []
    row.append(id_str)

    driver.get('https://break.co.kr/certification/' + id_str)

    try:
        element = WebDriverWait(driver, 0.0001, 0.0001).until(
            lambda x: x.find_element(By.CLASS_NAME , 'jss194')
        )
    except:
        print('Here is ' + id_str)
        continue
    else:
        element = driver.find_elements(By.CLASS_NAME, 'MuiTableCell-root')
        for i in range(0, len(element)):
            if i % 2 == 1:
                row.append(element[i].text)
        
        element = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/p[3]')
        row.append(element.text)

        element = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/p[3]')
        row.append(element.text)
        
        wr.writerow(row)

driver.quit()

f.close()