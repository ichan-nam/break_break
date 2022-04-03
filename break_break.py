import sys
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

if len(sys.argv) != 3:
    print("[Error] 사용법: python3 break_break.py 시작번호 검색개수")
    sys.exit()

start_id = int(sys.argv[1])
if start_id not in range(0, 10000000):
    print("[Error] 시작번호 범위 [0000000, 9999999]")
    sys.exit()

how_many = int(sys.argv[2])
if how_many < 0:
    print("[Error] 검색개수 >= 0")
    sys.exit()

end_bound = start_id + how_many 
if (end_bound > 10000000):
    end_bound = 10000000

f = open(str(start_id) + '-' + str(end_bound - 1) + '.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerow(['Id', 'Brand', 'Year', 'Set', 'Description', 'Card Number',
             'Player Name', 'Grade', 'Auto Grade', 'Population', 'Population Higher'])

service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)

for id in range(start_id, end_bound):
    id_str = str(id).zfill(7)

    row = []
    row.append(id_str)

    driver.get('https://break.co.kr/certification/' + id_str)

    try:
        element = WebDriverWait(driver, 0.0001, 0.0001).until(
            lambda x: x.find_element(By.CLASS_NAME , 'jss194')
        )
    except:
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