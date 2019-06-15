import unittest
from password import User

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
        self.assertEqual(self.new_user.password,"fifa")


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

#fourth test
    def test_delete_user(self):
            '''
            to test if we can remove a user from the user list
            '''
            self.new.new_user.save_user()
            test_user = User("Test","user","xyz")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)
if __name__ == '__main__':
    unittest.main()
