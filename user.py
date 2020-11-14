import keyring
import PySimpleGUI as SG
import platform
import os


class User:
    username = ''
    password = ''
    os = ''
    CRNs = []
    service_id = 'wwu-reg-app'
    USERNAME_KEY = 'cinema-voucher5-reattach'

    def __init__(self):
        username = SG.PopupGetText('Please type your username:', 'Username')
        password = SG.PopupGetText('Please type your password:', 'Password', password_char='*')
        keyring.set_password(self.service_id, username, password)

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
        # Query user for CRN
        # two conditions:
        # crn is not none
        # crn length is 5
        i = 0
        crn_num = i + 1
        has_crn = True
        while has_crn:
                if i > 2:
                    crn = SG.PopupGetText(f'Please type CRN {crn_num}, or none if you are done:',
                                          f'CRN {crn_num}')
                else:
                    crn = SG.PopupGetText(f'Please type CRN {crn_num}:', f'CRN {crn_num}')

                has_crn = ((len(crn) != 5) or ((crn is not "None") or (crn is not None)))
                self.CRNs[i] = crn
                i += 1
