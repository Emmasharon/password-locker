class User:
    '''
    Class that generates new instance of passwords
    '''
    users_list = []
    def __init_(self,first_name,last_name,password):
        '''
        __init__ method that helps us define properties the object holds.
        Args:
            first_name: New user first name.
            last_name : New user last name.
            number: New user phone number.
        '''

            #instance variables
            self.first_name: first_name
            self.last_name: last_name
            self.password: password

class Credentials:
    '''
    Class to let user add save or delete passwords
    '''
