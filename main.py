# Please only use this program in good faith.
# Software under the 0BSD license, aka do whatever you'd like with it!

import sched
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from user import User


# TODO: define function, separate out smaller functions
def run_bot(user):
    # Set browser to Chrome
    browser = webdriver.Chrome(user.os)

    # Go to registration page
    browser.get('https://admin.wwu.edu/pls/wwis/bwskfreg.P_AltPin')

    # Find username entry box
    username_entry = browser.find_element_by_xpath("""//*[@id="username"]""")
    # Send username to username entry box
    username_entry.send_keys(user.get_username())
    # Find password entry box
    password_entry = browser.find_element_by_xpath("""//*[@id="password"]""")
    # Send password to password entry box
    password_entry.send_keys(user.get_password())

    # Find "login" button, save to var
    login_button = browser.find_element_by_xpath("""//*[@id="fm1"]/section[4]/input[4]""")
    # Click "login" button
    login_button.click()

    # Find Term drop down menu
    termselect = Select(browser.find_element_by_xpath("""//*[@id="term_id"]"""))

    submit_button = browser.find_element_by_xpath("""/html/body/div[3]/form/input""")
    submit_button.click()

    CRN_id_num = 1
    for CRN in user.CRNs:
        crn_entry = browser.find_element_by_xpath(f"""//*[@id="crn_id{CRN_id_num}"]""")
        crn_entry.send_keys(CRN)
        CRN_id_num += 1

    submit_CRNs = browser.find_element_by_xpath("""/html/body/div[3]/form/input[19]""")
    submit_CRNs.click()


def run_bot_at_time(user: User):
    scheduler = sched.scheduler(time.localtime, time.sleep)
    scheduler.enterabs(time.strptime(user.registration_time), 0, run_bot)
    scheduler.run()


if __name__ == "__main__":
    user = User()
    cd = user.get_user_os()
    user.get_crn()
    run_bot_at_time(user)
