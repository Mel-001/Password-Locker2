class User:
    '''
    Class to create user instances 
    '''
    users_list = []

    def __init__ (self, user_name, password):

        '''
        properties of user 

        args:
        user_name
        password
        '''
        self.user_name = user_name
        self.password = password