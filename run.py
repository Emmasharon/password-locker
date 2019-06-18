#! /usr/bin/env python3
from password import User
from password import Credentials

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


# def verify_user(first_name,password):
# 	'''
# 	Function that verifies the existance of the user so as to create credentials
# 	'''
# 	verify_user = User.verify_user(first_name,password)
# 	return verify_user

def gen_password():
	'''
	Function to generate a password automatically
	'''
	gen_password = Credentials.gen_password()
	return gen_password

def create_credentials(account_name,password):
	'''
	Function to create a new credential instance
	'''
	new_credential=Credentials(account_name,password)
	return new_credential
	# Credentials.create_credentials(account_name,password)

def save_credentials(account_name,password):
	'''
	Function to save a new created credential
	'''
	Credentials.save_credentials(account_name,password)

def display_credentials(first_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credentials.display_credentials(first_name)

def copy_credential(account_name):
	'''
	Function to copy a credentials' details to the clipboard
	'''
	return Credentials.copy_credential(account_name)

def main():
	print(' ')
	print('Start by creating an account or log in if you have one.' )
	while True:
			print(' ')
			print("*"*100)
			print('Instructions: \n To create new account - new \n To login - log \n To exit - x')
			short_code = input('Enter a choice: ').lower().strip()
			if short_code == 'x':
				break
			elif short_code == 'new':
				print("*"*50)
				print(' ')
				print('create new account:')
				first_name = input('Enter first name - ').strip()
				last_name = input('Enter last name - ').strip()
				password = input('Enter your password - ').strip()
				save_user(create_user(first_name,last_name,password))
				print(" ")
				while True:
						print("*"*50)
						print('Navigation codes: \n cred-Add credentials to your account \n disp-Display credentials added \n copy-copy password to clipboard \n x-exit')
						short_code = input('Enter a choice: ').lower().strip()
						print("-"*50)
						if short_code == 'x':
							print(" ")
							print(f'Goodbye {first_name}')
							break
						elif short_code == 'cred':
							print(' ')
							print('Enter your credential details:')
							# site_name = input('Add a description: ').strip()
							account_name = input('Enter your account\'s name - ').strip()
							while True:
								print(' ')
								print("*"*50)
								print('Add password: \n mine-enter existing password \n rand-generate a random password \n x-exit')
								psword_choice = input('Select an option: ').lower().strip()
								print("-"*50)
								if psword_choice == 'mine':
									print(" ")
									password = input('Enter your password: ').strip()
									break
								elif psword_choice == 'rand':
									password = gen_password()
									break
								elif psword_choice == 'x':
									break
								else:
									print('You entered a wrong password. Try again')

							save_credentials(create_credentials(account_name, password))
							print(' ')
							print(f'Credential Created: Account Name: {account_name} - Password: {password} ')
							print(' ')
						elif short_code == 'disp':
							print(' ')
							if display_credentials(account_name, password):
								print('These are you saved accounts')
								print(' ')
								for credential in display_credentials(account_name, password):
									print(f'You have added: {credential.account_name} - Password: {credential.password}')
								print(' ')
							else:
								print(' ')
								print("You have no accounts saved")
								print(' ')
						elif short_code == 'copy':
							print(' ')
							account_name = input('What account do you want to copy ')
							copy_credential(account_name)
							print('')
						else:
							print('Oops! Wrong option entered. Try again.')

				else:
					print(' ')
					print('You have entered the wong details. Try again')

			else:
				print("*"*100)
				print(' ')
				print('Something went wrong. Try again.')

if __name__ == '__main__':
    main()
