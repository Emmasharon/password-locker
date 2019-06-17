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
