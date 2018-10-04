from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time
import decimal



#page = requests.get("http://sportsmodelanalytics.com/member/index.php?page=cbbbacktest",auth = ("sigepalbeta", "Albeta1927"))
#page


table = dict()

driver = webdriver.Chrome()
driver.get("http://sigepalbeta:Albeta1927@sportsmodelanalytics.com/member/index.php?page=mlbbacktest")
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
    control3 = 0
    controltable = decimal.Decimal('1.00')
    while controltable < 7.1:
        print(control1)
        print(control2)
        print(control3)
        print("Control table is: " + repr(controltable))
        inputElement = driver.find_element_by_id("min_value")
        inputElement.send_keys(control1)
        inputElement.send_keys('.')
        inputElement.send_keys(control2)
        inputElement.send_keys(control3)
        inputElement.send_keys(Keys.ENTER)
        print("just hit enter")
        inputElement1 = driver.find_element_by_id("min_value")
        time.sleep(1)
        #inputElement.send_keys("")
        time.sleep(1)
        inputElement1.send_keys(Keys.BACKSPACE)
        print("just hit back")
        inputElement2 = driver.find_element_by_id("min_value")
        inputElement2.send_keys(Keys.BACKSPACE)
        inputElement3 = driver.find_element_by_id("min_value")
        inputElement3.send_keys(Keys.BACKSPACE)
        inputElement4 = driver.find_element_by_id("min_value")
        inputElement4.send_keys(Keys.BACKSPACE)
        page = driver.page_source
        soup = BeautifulSoup(page)
        
        #print(page.status_code)
        #print(list(soup.children))
        
        want = soup.find_all('div', class_='well')[0].get_text()
        #print(list(want))
        
        length = len(want)
        print(want)
        print(length)

        strControl1 = str(control1)
        strControl2 = str(control2)
        strControl3 = str(control3)
        totalControl = strControl1 + '.' + strControl2 + strControl3

        value = float(totalControl)
        round (value, 2) 
        print("")
        print("won")
        print("____________")
        won = ""
        x = 0
        for x in range(0,5):
            won  = won + want[x]
            print(won)

        x = x + 1

        print("")
        print("wonTotal")
        print("____________")
        wonTotal = ''
        y = 0
        while is_number(want[x]) == True:
            wonTotal = wonTotal + want[x]
            x = x + 1
            y = y + 1
            print(wonTotal)

        IntWonTotal = int(wonTotal)
        x = x + 1

        print("")
        print("lost")
        print("____________")
        lost = ""
        z = 0
        for z in range(0,6):
            lost = lost + want[x]
            x = x + 1 
            print(lost)
        
        
        print("")
        print("lossTotal")
        print("____________")
        lostTotal = ''
        y = 0
        while is_number(want[x]) == True:
            lostTotal = lostTotal + want[x]
            x = x + 1
            y = y + 1
            print(lostTotal)

        intLostTotal = int(float(lostTotal))
        
        if IntWonTotal == 0 and intLostTotal == 0:
            break
        
        print("")
        print("totalUnits")
        print("____________")
        x = x + 1
        totalUnits = ""
        y = 0
        for y in range(0,13):
            totalUnits = totalUnits + want[x]
            x = x + 1
            y = y + 1
            print(totalUnits)

        
        
        print("")
        print("tu")
        print("____________")
        tu = ''
        y = 0
        while is_number(want[x]) == True or want[x] == '.' or want[x] == '-':
            tu = tu + want[x]
            x = x + 1
            y = y + 1
            print(tu)


        x = x + 1
        print("")
        print("ROI")
        print("____________")
        ROI = ""
        y = 0
        for y in range(0,5):
            ROI = ROI + want[x]
            x = x + 1
            y = y + 1
            print(ROI)

   
        print("")
        print("returnOI")
        print("____________")
        returnOI = ''
        y = 0
        while is_number(want[x]) == True or want[x] == '.'  or want[x] == '-':
            returnOI = returnOI + want[x]
            x = x + 1
            y = y + 1
            print(returnOI)
            if x == length:
            	break

        floatROI = float(returnOI)       
        returnOI = returnOI + '%'
            


        #print(won)
        #print(IntWonTotal)
        #print(lost)
        #print(intLostTotal)
        #print(totalUnits)
        #print(intTotalUnits)
        #print(ROI)
        #print(returnOI)
        #print(CLV)print(avgClv)

        if intLostTotal != 0 and floatROI > 8:
            struct = [value, returnOI,IntWonTotal,intLostTotal, (IntWonTotal/(IntWonTotal+intLostTotal)),tu]
            table[controltable] = struct
            print(struct)
        else:
            print("ROI < 8");
        
        control3 = control3 + 1
        x = decimal.Decimal('.01')
        controltable = controltable + x
        
        if (control3  == 10 ):
            control3 = 0
            control2 = control2 + 1
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

sheet = client.open("MLB TEST").sheet1
row = 132
col = 1

# Update values
count1 = 1
count2 = 1

k = decimal.Decimal('1.00')
l = 0

for count1 in range(131, 833):
    if k in table:
        print(table[k])
        for count2 in range(0,6):
            print( "row: %d" % row + "col: %d" % col)
        
            sheet.update_cell(row,col,table[k][l])
            col = col + 1
            l = l + 1

        row = row + 1
        x = decimal.Decimal('.01')

        k = k + x
        col = 1
        l = 0
    else:
        x = decimal.Decimal('.01')
        k = k + x
