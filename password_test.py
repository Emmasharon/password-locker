import unittest
from password import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behavioursself.

    Args:
        unitest.TestCase: TestCase class for creating test cases
    '''
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
