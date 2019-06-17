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
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}.Choose an option to continue')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cred-Add credentials to your account \n disp-Display credentials added \n copy-copy password to clipboard \n x-exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'x':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cred':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Add password: \n mine-enter existing password \n rand-generate a random password \n x-exit')
							psw_choice = input('Select an option: ').lower().strip()
							print("-"*60)
							if psword_choice == 'mine':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psword_choice == 'new':
								password = generate_password()
								break
							elif psword_choice == 'x':
								break
							else:
								print('You entered a wrong password. Try again')
						save_credential(create_credential(user_name,account_name,password))
						print(' ')
						print(f'Credential Created: Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'disp':
						print(' ')
						if display_credentials(user_name):
							print('These are you saved accounts')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')
						else:
							print(' ')
							print("You have no accounts saved")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('What account do you want to copy ')
						copy_credential(chosen_account)
						print('')
					else:
						print('Oops! Wrong option entered. Try again.')

			else:
				print(' ')
				print('You have entered the wong details. Try again')

		else:
			print("-"*60)
			print(' ')
			print('Something went wrong. Try again.')







if __name__ == '__main__':
    main()
