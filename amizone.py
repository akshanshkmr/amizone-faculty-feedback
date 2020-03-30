from pynput.mouse import Button, Controller
import time
from selenium import webdriver
import os
import sys

print("Amizone feedback tool (2020), By: Akshansh Kumar,AIIT")
uid         = input("Enter your amizone id:")
passw       = input("Enter your password:")
comments    = input("Enter your comments:")
rating      = input("Enter your rating(1=Strongly agree...5=Strongly disagree):")#  1=Strongly Agree, 2=Agree, 3=Neutral, 4=Disagree,5=Strongly Disagree

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'))
driver.maximize_window()
driver.get("https://www.amizone.net")
driver.find_element_by_name('_UserName').send_keys(uid)
driver.find_element_by_name('_Password').send_keys(passw)
driver.find_element_by_class_name('login100-form-btn').click()
time.sleep(2)
mouse=Controller()
#clicks on a blank spot on webpage to clear the pop up mesages
mouse.position=(254,140)
for i in range(5):
    mouse.press(Button.left)
    mouse.release(Button.left)
driver.find_element_by_id('27').click() #option for faculty feedback in list
time.sleep(1)

def fill(n=1):
    try:
        for i in range(1,10):
            driver.find_element_by_xpath('//*[@id="form0"]/div/div//div['+str(n)+']/div[2]/div/div/table/tbody/tr['+str(i)+']/td['+str(rating+2)+']').click()
    except:
        if (n > 10):
            return
        else:
            fill(n+1)

def yesno():
    driver.find_element_by_id('rdbQuestion1').click()
    driver.find_element_by_id('rdbQuestion2').click()
    driver.find_element_by_id('rdbQuestion3').click()

def comment():
    driver.find_element_by_id('FeedbackRating_Comments').send_keys(comments)

def submit():
    driver.find_element_by_id('btnSubmit').click()

def main(n=1):
    try:
        for i in range(n,20):
            time.sleep(1)
            #click on the faculty
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li['+ str(i)+']').click()
            # click on the fill feedback button
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li['+str(i)+']/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/a').click()
            time.sleep(2)
            driver.execute_script('window.scrollTo(0,0)')
            time.sleep(2)
            fill()
            comment()
            submit()
            time.sleep(1)
    except:
        time.sleep(1)
        driver.execute_script('window.scrollTo(0,0)')
        time.sleep(1)
        main(n+1)

if __name__ =="__main__":
    main()