import pyperclip
import random
import string

global users_list

class User:
    '''
    Class that generates new instance of passwords
    '''
    users_list = []


    def __init__(self,first_name,last_name,password):
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


    # @classmethod
    # def verify_user(cls,first_name,password):
    #     '''
    #     to verify user
    #     '''
    #     for user in cls.users_list:
    #         if User.first_name == first_name and User.password == password:
    #             return user

    def save_user(self):
        '''
        save user objects into users_list
        '''

        User.users_list.append(self)



class Credentials:
    '''
    Class to let user create class credentials, save credentials and generate passwords
    '''
    credentials_list = []

    def __init__(self,account_name,password):
        '''
        __init__ method that helps us define properties the object holds
        Args:

            account_name: New credential name.
            password: New credential password

        '''
        # self.first_name: first_name
        self.account_name: account_name
        self.password: password

    @classmethod
    def save_credentials(self):
        '''
        save credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self,account_name,password)

    @classmethod
    def create_credentials(self):
        '''
        create credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    @classmethod
    def copy_credentials(cls, account_name):
        '''
        Method that takes account_name and returns details matching that account_name
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def display_credentials(cls, account_name):
        '''
        Method to display the list of credential that has been save_credentials
        '''
        for credential in cls.credentials_list:
            if credential.first_name == account_name:
                cls.credentials_list.append()
                return cls.credentials_list

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Method to take in account name and return credentials for that account
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def copy_credential(cls, account_name):
        '''
        Class method that copies a credential's info after the credential's account name is entered
        '''
        find_credential = Credentials.find_by_account_name(account_name)

        return pyperclip.copy(find_credential.password)

    @classmethod
    def gen_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate random password with six digits
        '''
        gen_password = ''.join(random.choice(char) for _ in range(size))
        return gen_password
