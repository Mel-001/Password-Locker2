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
    def search_user_credentials(cls, user_account):

        '''
        method that searches user credentials
        '''
        
        for credential in cls.credentials_list:
            if credential.user_account == user_account:
                return credential
            @classmethod
            def show_credentials(cls):

        '''
        function displays user credentials
        '''


        return cls.credentials_list