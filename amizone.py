from time import sleep
from selenium import webdriver
import os
import sys, traceback

print("Amizone feedback tool (2020), By: Akshansh Kumar, AIIT")
uid         = input("Enter your amizone id:")
passw       = input("Enter your password:")
comments    = input("Enter your comments:")
rating      = int(input("Enter your rating(5=Strongly agree...1=Strongly disagree):"))
#  5=Strongly Agree, 4=Agree, 3=Neutral, 2=Disagree, 1=Strongly Disagree

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# open browser and go to amizone
try:
    driver = webdriver.Edge(resource_path('./driver/msedgedriver.exe'))
except Exception as e:
    print('\033[91m'+'Browser/Webdriver Mismatch Found!'+'\033[0m')
    print('\033[93m'+str(e).strip()+'\033[0m')
    print('\033[96m'+'Please ensure you are running an updated version of Microsoft Edge (Chromium)'+'\033[0m')
    print('Download here: '+'\033[92m'+'https://www.microsoft.com/en-us/edge'+'\033[0m')
    print('\033[96m'+'Also ensure that you have the correct version of webdriver that matches your browser version'+'\033[0m')
    print('Download here: '+'\033[92m'+'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/'+'\033[0m')
    print('\033[93m'+'Then, Replace the "msedgedriver.exe" file present in: '+'\033[92m'+os.path.dirname(__file__)+'/driver/'+'\033[0m')
    sys.exit()
driver.maximize_window()

def visit_amizone():
    driver.get("https://www.amizone.net")
    # login to amizone
    driver.find_element_by_name('_UserName').send_keys(uid)
    driver.find_element_by_name('_Password').send_keys(passw)
    driver.find_element_by_class_name('login100-form-btn').click()

def verify_login():
    # verify login
    sleep(2)
    if driver.current_url != 'https://s.amizone.net/Home':
        driver.close()
        raise Exception('\033[91m'+'Login Failed! Please check your ID/Password!'+'\033[0m')
    else:
        print('\033[94m'+'Login Successful!'+'\033[0m')

def close_popups():
    # close pop-ups
    try:
        sleep(2)
        popups=driver.find_elements_by_class_name("close")
        print(str(len(popups))+" Pop-ups found!")
        for close_btn in popups:
            try:
                close_btn.click()
            except:
                print('\033[93m'+u'\u2717',end=" ")
            else:
                print('\033[92m'+u'\u2713',end=" ")
    except:
        print('\033[94m'+"No Pop-ups found!"+'\033[0m')
    else:
        print('\033[92m'+"\nAll Pop-ups closed!"+'\033[0m')

def select_my_faculty():
    #option for faculty feedback in list
    try:
        sleep(2)
        driver.find_element_by_id('M27').click() 
        sleep(1)
    except:
        print('\033[92m'+'No Faculty Feedback Exists for you!'+'\033[0m')

def fill():
    driver.execute_script("var items = document.querySelectorAll('input[value=\""+str(rating)+"\"]');for (var i = 0; i < items.length; i++) {items[i].click();}")

def yesno():
    driver.execute_script("document.querySelectorAll('input[id=\"rdbQuestion1\"]')[0].click();")
    driver.execute_script("document.querySelectorAll('input[id=\"rdbQuestion2\"]')[0].click();")
    driver.execute_script("document.querySelectorAll('input[id=\"rdbQuestion3\"]')[0].click();")

def comment():
    driver.find_element_by_id('FeedbackRating_Comments').send_keys(comments)

def submit():
    driver.find_element_by_id('btnSubmit').click()

def fill_feedback():
    for subj in driver.find_elements_by_class_name('subject'):
        sleep(1)
        subj.click()
        sleep(1)
        try:
            driver.find_element_by_css_selector('[title="Please click here to give faculty feedback"]').click()
        except:
            pass
        else:
            sleep(1)
            fill()
            yesno()
            comment()
            submit()

def main():
    visit_amizone()
    verify_login()
    close_popups()
    select_my_faculty()
    try:
        fill_feedback()
    except:
        sleep(5)
        fill_feedback()
    

if __name__ =="__main__":
    main()
    print('\033[92m'+'Feedback Successfully filled! PLease verify manually.'+'\033[0m')
    print('\033[93m'+'[NOTE]:If some faculties are left, you can re-run the script'+'\033[0m')