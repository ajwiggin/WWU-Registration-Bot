import keyring
import PySimpleGUI as SG
import platform
import os
class User:
    username = ''
    password = ''
    os = ''
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
        user_os = platform.system()
        if "Darwin" in user_os:
            user_os = "Mac"
            cd = "chromedriverMac"
        if "Windows" in user_os:
            user_os = "windows"
            cd = "chromedriverWindows"

        user_path = os.getcwd()
        cd = str(user_path) + "/" + cd

        return user_os
