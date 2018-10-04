from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time



#page = requests.get("http://sportsmodelanalytics.com/member/index.php?page=cbbbacktest",auth = ("sigepalbeta", "Albeta1927"))
#page


table = dict()

driver = webdriver.Chrome()
driver.get("http://sigepalbeta:Albeta1927@sportsmodelanalytics.com/member/index.php?page=nbabacktest")
#page = driver.page_source

#inputElement = driver.find_element_by_id("min_diff")
#inputElement.send_keys('1')
#inputElement.send_keys(Keys.ENTER)
####################3
# declaring two functions used


def find(driver):
    element = driver.find_elements_by_id("data")
    if element:
        return element
    else:
        return False


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


def scrapeify (*x):
    
    
    
    
    control1 = 1
    control2 = 0
    controltable = 1.0
    while controltable < 7.1:
        inputElement = driver.find_element_by_id("min_diff")
        inputElement.send_keys(control1)
        inputElement.send_keys('.')
        inputElement.send_keys(control2)
        inputElement.send_keys(Keys.ENTER)
        print("just hit enter")
        inputElement1 = driver.find_element_by_id("min_diff")
        time.sleep(1)
        #inputElement.send_keys("")
        time.sleep(1)
        inputElement1.send_keys(Keys.BACKSPACE)
        print("just hit back")
        inputElement2 = driver.find_element_by_id("min_diff")
        inputElement2.send_keys(Keys.BACKSPACE)
        inputElement3 = driver.find_element_by_id("min_diff")
        inputElement3.send_keys(Keys.BACKSPACE)
        page = driver.page_source
        soup = BeautifulSoup(page)
        
        #print(page.status_code)
        #print(list(soup.children))
        want = soup.find_all('div', class_='well')[0].get_text()
        
        #print(list(want))
        
        length = len(want)
        print(want)
        #print(length)

        won = ""
        x = 0
        for x in range(0,6):
            won  = won + want[x]
            print(won)

        x = x + 1
        wonTotal = ''
        y = 0
        while is_number(want[x]) == True:
            wonTotal = wonTotal + want[x]
            x = x + 1
            y = y + 1
            print(wonTotal)

        IntWonTotal = int(wonTotal)

        lost = ""
        z = 0
        for z in range(0,7):
            lost = lost + want[x]
            x = x + 1 
            print(lost)


        lostTotal = ''
        y = 0
        while is_number(want[x]) == True:
            lostTotal = lostTotal + want[x]
            x = x + 1
            y = y + 1
            print(lostTotal)

        intLostTotal = int(lostTotal)

        totalUnits = ""
        y = 0
        for y in range(0,14):
            totalUnits = totalUnits + want[x]
            x = x + 1
            y = y + 1
            print(totalUnits)

        tu = ''
        y = 0
        while is_number(want[x]) == True or want[x] == '.' or want[x] == '-':
            tu = tu + want[x]
            x = x + 1
            y = y + 1
            print(tu)


        ROI = ""
        y = 0
        for y in range(0,6):
            ROI = ROI + want[x]
            x = x + 1
            y = y + 1
            print(ROI)

        returnOI = ''
        y = 0
        while is_number(want[x]) == True or want[x] == '.' or want[x] == '%' or want[x] == '-':
            returnOI = returnOI + want[x]
            x = x + 1
            y = y + 1
            print(returnOI)

        CLV = ""
        y = 0
        for y in range(0,10):
            CLV = CLV + want[x]
            x = x + 1
            y = y + 1
            print(CLV)

        avgClv = ''
        y = 0

        while is_number(want[x]) == True or want[x] == '.' or want[x] == '-':
            avgClv = avgClv + want[x]
            if x  == length-1:
                break
            x = x + 1
            y = y + 1
            print(avgClv)
            


        #print(won)
        #print(IntWonTotal)
        #print(lost)
        #print(intLostTotal)
        #print(totalUnits)
        #print(intTotalUnits)
        #print(ROI)
        #print(returnOI)
        #print(CLV)print(avgClv)

        if intLostTotal != 0:
            struct = [returnOI,IntWonTotal,intLostTotal, (IntWonTotal/(IntWonTotal+intLostTotal)),tu]
            print(struct)
        else:
            struct = [0,0,0,0,0]
        table[controltable] = struct
        control2 = control2 + 1
        controltable = controltable + 0.1
        if (control2  == 10):
            control2 = 0
            control1 = control1 + 1

#################################################

scrapeify(1)
print(table)

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']


creds = ServiceAccountCredentials.from_json_keyfile_name('My Project-edaceacb1aea.json', scope)
client = gspread.authorize(creds)

sheet = client.open("ROI SMA").sheet1
row = 1
col = 1

# Update values
count1 = 1
count2 = 1
k = 1
l = 0

for count1 in range(1, 70):
    print(table[k])
    for count2 in range(0,6):
        print( "row: %d" % row + "col: %d" % col)
        print(k)
        if col == 1:
            sheet.update_cell(row,col,k)
            col = col + 1
        else:
            sheet.update_cell(row,col,table[k][l])
            col = col + 1
            l = l + 1

    row = row + 1
    k = k + .1
    col = 1
    l = 0
