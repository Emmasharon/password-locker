import unittest
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

        def  test_check_user(self):
            '''
            Function to check if the login function works well
            '''
            self.new_user = User('olweezy','rachy','xyz100')
            self.new_user.save_user()
            user@ = User('olweezy','rachy','xyz100')
            user@.save_user()
            for user in User.users_list:
                if user.first_name == user@.first_name and user.password == user@.password:
                    current_user == user.first_name
                    return current_user

            self.assertEqual(current_user,Credential.check_user(user@.password,user@.first_name))


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
