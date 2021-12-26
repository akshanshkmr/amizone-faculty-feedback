from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from rich.console import Console
import sys

console = Console()

def pprint(*args, **kwargs):
    console.print(*args, **kwargs)

pprint("-------------------------------------------------------", style='b blue')
pprint("Amizone feedback tool (2020), By: Akshansh Kumar, AIIT", style='b blue')
pprint("-------------------------------------------------------", style='b blue')

uid         = input("Enter your amizone id:")
passw       = input("Enter your password:")
comments    = input("Enter your comments:")
rating      = int(input("Enter your rating(5=Strongly agree ... 1=Strongly disagree):"))

driver = webdriver.Chrome(ChromeDriverManager().install())
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
        pprint("Login Failed! Please check your ID/Password!", style='b red')
        sys.exit()
    else:
        pprint('Login Successful!', style='b green')

def close_popups():
    # close pop-ups
    try:
        sleep(2)
        popups=driver.find_elements_by_class_name("close")
        pprint(str(len(popups))+" Pop-ups found!", style='b yellow')
        for close_btn in popups:
            try:
                close_btn.click()
            except:
                pprint('✘', style='b red', end=' ')
            else:
                pprint('✔', style='b green', end=' ')
    except:
        pprint("No Pop-ups found!", style='b green')
    else:
        pprint("All Pop-ups closed!", style='b green')

def select_my_faculty():
    #option for faculty feedback in list
    try:
        sleep(2)
        driver.find_element_by_id('M27').click() 
        sleep(1)
    except:
        pprint('No Faculty Feedback Exists for you!', style='b green')

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
    close_popups()
    select_my_faculty()
    try:
        fill_feedback()
    except:
        sleep(5)
        fill_feedback()
    
if __name__ =="__main__":
    main()
    pprint('Feedback Successfully filled! PLease verify manually.', style='b green')
    pprint('[NOTE]:If some faculties are left, you can re-run the script', style='b yellow')