"""
    Check input.data are valid or not
"""
import re
from lib.language.en import email_invalid, password_not_same, password_invalid


class ValidChecker(object):
    is_valid = True
    error = ''

    def email_check(self, email):
        is_match = bool(re.match(r'^[\d\w.]+@[\d\w.{1}]+.[\d\w]{2,}$', email))
        #not a good email match
        if not is_match:
            self.is_valid = False
            self.error += email_invalid

    def password_check(self, password, en_password):
        if not password == en_password:
            self.is_valid = False
            self.error += password_not_same

    def password_valid_check(self, password):
        if len(password) < 6 or len(password) > 16:
            self.is_valid = False
            self.error += password_invalid


class RegValidChecker(ValidChecker):
    def __init__(self, input_data):
        self.email_check(input_data.email)
        self.password_valid_check(input_data.password)
        self.password_check(input_data.password, input_data.en_password)


