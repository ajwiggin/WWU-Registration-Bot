import keyring
import PySimpleGUI as SimpleGUI
import platform
import os


class User:
    username = ''
    registration_time = 0
    os = ''
    CRNs = []
    service_id = 'wwu-reg-app'
    USERNAME_KEY = 'cinema-voucher5-reattach'

    def __init__(self):
        self.username = SimpleGUI.PopupGetText('Please type your username:', 'Username')
        password = SimpleGUI.PopupGetText('Please type your password:', 'Password', password_char='*')
        self.registration_time = SimpleGUI.PopupGetText('Please type in your registration time (Ex: Tue '
                                                 'May 01 11:20:20 2020)', 'Registration Time')
        keyring.set_password(self.service_id, self.username, password)

    def get_username(self):
        return keyring.get_password(self.service_id, self.USERNAME_KEY)

    def get_password(self):
        return keyring.get_password(self.service_id, self.username)

    # TODO: check if this legacy code
    def get_user_os(self):
        cd = ''
        user_os = platform.system()
        if "Darwin" in user_os:
            user_os = "Mac"
            cd = "chromedriverMac"
        if "Windows" in user_os:
            user_os = "windows"
            cd = "chromedriverWindows"

        user_path = os.getcwd()
        cd += str(user_path) + "/"

        return user_os

    def get_crn(self):
        i = 0
        crn_num = i + 1
        has_crn = True
        while has_crn:
            if i > 2:
                crn = SimpleGUI.PopupGetText(f'Please type CRN {crn_num}, or none if you are done:',
                                      f'CRN {crn_num}')
            else:
                crn = SimpleGUI.PopupGetText(f'Please type CRN {crn_num}:', f'CRN {crn_num}')

            has_crn = ((len(crn) != 5) or ((crn is not "None") or (crn is not None)))
            self.CRNs[i] = crn
            i += 1
