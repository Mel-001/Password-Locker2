from details.user import User
from details.credentials import Credentials
import sys

def create_new_user(user_name, password):
    '''
 function that creates a new user instance
    '''
    new_user = User(user_name, password)

    return new_user
def save_new_user(user):
    user.save_this_user
def show_user(user):
    '''
    this function displays a user
    '''
    user.show_user()
    def acc_login(user_name, password):
    '''
    function that validates user login by calling the validate function in the credentials class
    '''
    return User.validate_user(user_name, password
                              def create_credentials(user_account,user_name, password):
    '''
    create a credentials user account
    '''
    new_credentials = Credentials(user_account, user_name,password)
    return new_credentials
def save_credentials(credentials_list):
    Credentials.save_credentials(credentials_list)
