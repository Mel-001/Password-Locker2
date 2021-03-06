class User:
    '''
    This is a class to create instances of a user
    '''

    #empty users list
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

    def save_this_user(self):
        '''
        this method adds a user to the list
        '''
        User.users_list.append(self)
        
    @classmethod
    def show_user(cls):
        '''
        return user list

        '''
        return cls.users_list
        
    def find_user_name(cls, user_name):
        '''
        function to find a user by their user name
        '''

        for user in cls.users_list:
            if user.user_name == user_name:
                return user_name

    @classmethod
    def validate_user(cls,user_name, password):
        '''
        this functions validates user login
        '''
        for user in cls.users_list:
            if user.user_name == user_name and user.password == password:
                return user
            