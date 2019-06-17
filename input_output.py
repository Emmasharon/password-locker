import pyperclip
from locker import User, Credential

def create_user(first_name,last_name,password):
	'''
	Function to create a new user account
	'''
	new_user = User(first_name,last_name,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user so as to create credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_password = Credential.generate_password()
	return gen_pass

def create_credential(user_name,account_name,password):
	'''
	Function to create a new credential instance
	'''
	new_credential=Credential(user_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a new created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)

def copy_credential(site_name):
	'''
	Function to copy a credentials' details to the clipboard
	'''
	return Credential.copy_credential(account_name)

def main():
    print(' ')
    print('WELCOME TO PASSWORD-LOCKER')
    while True:
        print(' ')
        print('This is a cool program that lets you store all your passwords in one single account.')
def main():
	print(' ')
	print('Start by creating an account or log in if you have one.')
	while True:
		print(' ')
		print("-"*60)
		print('Instructions: \n To create new account - new \n To login - log \n To exit - x')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'x':
			break

		elif short_code == 'new':
			print("-"*60)
			print(' ')
			print('create new account:')
			first_name = input('Enter first name - ').strip()
			last_name = input('Enter last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'log':
			print("-"*60)
			print(' ')
			print('Enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			
