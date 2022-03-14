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