import unittest
import pyperclip
from password import User
from password import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behavioursself.

    Args:
        unitest.TestCase: TestCase class for creating test cases
    '''
#first test
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("olweezy","rachy","fifa")


    def test_init(self):
        '''
        test_init test if the obeject is initialized well
        '''
        self.assertEqual(self.new_user.first_name,"olweezy")
        self.assertEqual(self.new_user.last_name,"rachy")
        self.assertEqual(self.new_user.password,"fifa247")


        if __name__ == '__main__':
            unittest.main()

#second test
    def test_save_user(self):
        '''
        test case to test if the user object is saved into the user users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
    if __name__ == '__main__':
        unittest.main()

# #fourth test
#     def test_delete_user(self):
#             '''
#             to test if we can remove a user from the user list
#             '''
#             self.new.new_user.save_user()
#             test_user = User("Test","user","xyz")
#             test_user.save_user()
#
#             self.new_user.delete_user()
#             self.assertEqual(len(User.user_list),1)
#     if __name__ == '__main__':
#          unittest.main()

    # def delete_user(self):
    #
    # '''
    # delete_user method deletes a saved contact from the user_list
    # '''
    #
    # User.user_list.remove(self)

    class TestCredentials(unittest.TestCase):
        '''
        Test class for testing cases of the credentials class behaviour
        Args:
            unitest.TestCase: TestCase class for creating test cases
        '''

        def  test_verify_user(self):
            '''
            Function to check if the login function works well
            '''
            self.new_user = User('olweezy','rachy','xyz100')
            self.new_user.save_user()
            userx = User('olweezy','rachy','xyz100')
            userx = save_user()
            for user in User.users_list:
                if user.first_name == userx.first_name and user.password == userx.password:
                    current_user == user.first_name
                    return current_user

            self.assertEqual(current_user,Credential.verify_user(userx.password,userx.first_name))


        def setUp(self):
            '''
            Create an account's credentials before each testing
            '''
            self.new_credential = Credential('olweezy','twitter','xyz100')

        def test_init(self):
            '''
            test_init test if the object is initialized well
            '''
            self.assertEqual(self.new_credential.user_name,"olweezy")
            self.assertEqual(self.new_credential.account_name,"twitter")
            self.assertEqual(self.new_credential.account_password,"xyz100")


            if __name__ == '__main__':
                unittest.main()

        def test_save_user(self):
            '''
            test case to test if the credentials object is saved into the credentials_list
            '''
            self.new_credential.save_credentials()
            facebook = Credential('olweezy','facebook','xyz100')
            self.assertEqual(len(Credential.credentials_list), 2)
            if __name__ == '__main__':
                unittest.main()

        def tearDown(self):
            '''
            Function to clear the credentials list after every test
            '''
            Credential.credentials_list = []
            User.users_list = []

        def test_display_credentials(self):
            '''
            Test to check if the display_credentials method displays the correct credentials.
            '''
            self.new_credential.save_credentials()
            facebook = Credential('ray', 'facebook', 'xyz100')
            facebook.save_credentials()
            instagram = Credential('olweezy', 'Instagram', 'abc100')
            instagram.save_credentials()
            self.assertEqual(
                len(Credential.display_credentials(facebook.user_name)), 3)

        def test_find_by_site_name(self):
            '''
            Test to check if the find_by_site_name method works
            '''
            self.new_credential.save_credentials()
            facebook = Credential('olweezy', 'facebook', 'xyz100')
            twitter.save_credentials()
            credential_exists = Credential.find_by_site_name('facebook')
            self.assertEqual(credential_exists, facebook)

        def test_copy_credential(self):
            '''
            Test to check if the copy a credential method copies the correct credential
            '''
            self.new_credential.save_credentials()
            facebook = Credential('olweezy', 'facebook', 'xyz100')
            twitter.save_credentials()
            find_credential = None
            for credential in Credential.user_credentials_list:
                find_credential = Credential.find_by_account_name(
                    credential.account_name)
                return pyperclip.copy(find_credential.password)
            Credential.copy_credential(self.new_credential.account_name)
            self.assertEqual('xyz100', pyperclip.paste())
            print(pyperclip.paste())

        if __name__ == '__main__':
            unittest.main()
