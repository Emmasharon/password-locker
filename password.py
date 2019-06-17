# import pyperclip
import random
import string

global users_list

class User:
    '''
    Class that generates new instance of passwords
    '''
    users_list = []
    def save_user(self):
        '''
        save user objects into users_list
        '''

        User.users_list.append(self)


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

class Credentials:
    '''
    Class to let user create class credentials, save credentials and generate passwords
    '''
    credentials_list = []
    def save_credentials(self):
        '''
        save credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def __init__(self,user_name,account_name,account_password):
        '''
        __init__ method that helps us define properties the object holds
        Args:
            user_name: user_name.
            account_name: New accout name.
            account_password: New account password.
        '''
        user_name: user_name
        self.account_name: account_name
        self.account_password: account_password

    @classmethod
    def copy_credentials(cls, account_name):
        '''
        Method that takes account_name and returns details matching that account_name
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credentials_list

    @classmethod
    def display_credential(cls,user_name):
        '''
        Method to display the list of credential that has been save_credentials
        '''
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
                return user_credentials_list

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Method to take in account name and return credentials for that account
        '''
        for credential in cls.credentials_list:
            if credential.site_name == account_name:
                return credentials_list

    @classmethod
    def copy_credential(cls, site_name):
        '''
        Class method that copies a credential's info after the credential's account name is entered
        '''
        find_credential = Credential.find_by_account_name(account_name)

        return pyperclip.copy(find_credential.password)

    @classmethod
    def generate_password(size=6, char=string + string.digits):
        '''
        Function to generate random password with six digits
        '''
        gen_password = ''.join(random.choice(char) for _ in range(size))
        return gen_password
