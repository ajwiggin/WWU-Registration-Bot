# Please only use this program in good faith.
# Software under the 0BSD license, aka do whatever you'd like with it!

import sched
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from user import User


# TODO: define function, separate out smaller functions
def run_bot(user):
    # Set browser to Chrome
    # TODO: Chromium isn't currently working, using safari for now
    # browser = webdriver.Chrome(user.os)
    browser = webdriver.Safari()

    wait = lambda xpath : WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # Go to registration page
    browser.get('https://admin.wwu.edu/pls/wwis/bwskfreg.P_AltPin')

    # Find username entry box
    username_entry = wait("""//*[@id="username"]""")
    # Send username to username entry box
    username_entry.send_keys(user.get_username())
    # Find password entry box
    password_entry = wait("""//*[@id="password"]""")
    # Send password to password entry box
    password_entry.send_keys(user.get_password())

    # Find "login" button, save to var
    login_button = wait("""//*[@id="fm1"]/section[4]/input[4]""")
    # Click "login" button
    login_button.click()

    # Find Term drop down menu
    termselect = wait("""//*[@id="term_id"]""")

    submit_button = wait("""/html/body/div[3]/form/input""")
    submit_button.click()

    CRN_id_num = 1
    for CRN in user.CRNs:
        crn_entry = wait(f"""//*[@id="crn_id{CRN_id_num}"]""")
        crn_entry.send_keys(CRN)
        CRN_id_num += 1

    submit_CRNs = wait("""/html/body/div[3]/form/input[19]""")
    submit_CRNs.click()


def run_bot_at_time(user: User):
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enterabs(time.mktime(user.registration_time), 1, run_bot, [user])
    scheduler.run()
