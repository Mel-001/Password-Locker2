from .user import User
import string
import random

class Credentials:
    '''
    add credentials to the credentials list
    '''
    credentials_list = []

    def __init__ (self, user_account, user_name, password):
        '''
        properties of credentials

        args:
        user_account
        user_name
        password

        '''
        self.user_account = user_account
        self.user_name = user_name
        self.password = password
        
        def save_credentials(self):

        '''
        add new credential to credentials_list
        '''

        Credentials.credentials_list.append(self)

    @classmethod 