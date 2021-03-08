import keyring, time
import PySimpleGUI as SimpleGUI
import platform
import os


class User:
    username = ''
    registration_time = 0
    driver_path = ''
    CRNs = []
    service_id = 'wwu-reg-app'

    def __init__(self):
        self.username = get_input('Please type your username:', 'Username')
        password = get_input('Please type your password:', 'Password', password_char='*')
        keyring.set_password(self.service_id, self.username, password)
        # Get and validate registration time
        while True:
            timeStr = get_input('Please type in your registration time (Ex: March 3 2021 7:40 AM):', 'Registration Time')
            try:
                self.registration_time = time.strptime(timeStr, '%B %d %Y %I:%M %p')
            except ValueError:
                print("Invalid date/time input.")
                continue
            break
        # Get CRNs
        while len(self.CRNs) <= 10:
            if (len(self.CRNs) < 1):
                thisCRN = get_input("Enter CRN " + str(len(self.CRNs)+1) + "/10:", "CRN"  + str(len(self.CRNs)+1), allowEmptyInput=True)
            else:
                thisCRN = get_input("Enter CRN " + str(len(self.CRNs)+1) + "/10 ([enter] if finished):", "CRN"  + str(len(self.CRNs)+1), allowEmptyInput=True)
            if thisCRN == "":
                if (len(self.CRNs) == 0): continue
                else: break
            if thisCRN.isnumeric() and len(thisCRN) == 5:
                self.CRNs.append(thisCRN)
        # Get OS
        cwd = os.path.abspath(os.getcwd())
        print(cwd)
        system = platform.system()
        if (system == "Darwin"):
            driver_path = cwd + "drivers/chromedriverIntelMac"
        elif (system == "Windows"):
            driver_path = cwd + "drivers/chromedriverWindows.exe"
        elif (system == "Linux"):
            driver_path = cwd + "drivers/chromedriverLinux"
        else:
            driver_path = cwd + "drivers/chromedriverWindows"
            print("System not Windows or Mac, using Windows chromedriver.")
        print(driver_path)

    def get_username(self):
        return self.username

    def get_password(self):
        return keyring.get_password(self.service_id, self.username)

def get_input(message, title=None, password_char='', allowEmptyInput=False):
    hasInvalid = False
    while True:
        thisInput = thisInput = SimpleGUI.PopupGetText(message, title, password_char=password_char)
        if allowEmptyInput:
            return thisInput
        elif thisInput == "":
            message = message if hasInvalid else "Invalid input. " + message
            continue
        return thisInput
