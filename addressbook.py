import pickle
import os

def load_book(filename):
	# load the contact list from the file
	with open(filename, 'rb') as address_book:
		# check if the file is empty and initialize it to empty list if file empty
		is_file_empty = os.path.getsize(filename)==0
		if not is_file_empty:
			contact_list = pickle.load(address_book)
		else:
			contact_list = []

	return contact_list

def store_book(contact_list, filename):
	# store the contact list to the file
	with open(filename, 'wb') as address_book:

		pickle.dump(contact_list, address_book)

def add_contact(contact_list):
	# add new contact to contact list
	# create a dictionary for the contact
	contact = {}
	contact['name'] = input('Enter full name: ').strip().lower()
	contact['email'] = input('Enter the email: ').strip()
	contact['phone'] = input('Enter the phone number: ').strip()
	contact_list.append(contact)

def delete_contact(contact_list):
	# delete contact from contact list
	# search contact from the list
	
	print('Search for a contact to delete:')
	contact = search_contact(contact_list)[0]
	print('{:<30}{:<30}{:<30}'.format(contact['name'].capitalize(), contact['email'], contact['phone']))
	delete = input('Do you want to delete above contact(Y/N):').strip().lower() 
	if delete == 'y':
		contact_list.remove(contact)

def search_contact(contact_list):

	search_options = ['name', 'email', 'phone']
	print('How would you like to search')
	print('\t\t{:<20}'.format('1. Search by name'))
	print('\t\t{:<20}'.format('2. Search by email'))
	print('\t\t{:<20}'.format('3. Search by phone'))
	search_by = search_options[int(input())-1]
	search_string = input('Which {} do you want to search: '.format(search_by)).strip().lower()

	return list(filter(lambda person: person[search_by].find(search_string) != -1, contact_list))

def update_contact(contact_list):

	print('Search for a contact to update:')
	old_contact = search_contact(contact_list)[0]
	contact_list.remove(old_contact)

	if input('Do you want to update contact name(Y/N): ').strip().lower() == 'y':
		old_contact['name'] = input('Update name to: ').strip().lower()

	if input('Do you want to update contact email(Y/N): ').strip().lower() == 'y':
		old_contact['email'] = input('Update email to: ').strip().lower()

	if input('Do you want to update contact phone number(Y/N): ').strip().lower() == 'y':
		old_contact['phone'] = input('Update phone number to: ').strip().lower()

	contact_list.append(old_contact)

def show_contacts(contact_list):

	print('{:<30}{:<30}{:<30}'.format('NAME:', 'EMAIL:', 'PHONE NUMBER:'))
	print()
	for contact in contact_list:
		print('{:<30}{:<30}{:<30}'.format(contact['name'].capitalize(), contact['email'], contact['phone']))
	print()

def main():

	filename = 'address_book'
	contact_list = load_book(filename)

	inp_opt = None
	
	while inp_opt != '5':

		if input('Would you like to display a current list of contacts?(Y/N): ').strip().lower() == 'y':
			show_contacts(contact_list);

		print('What would you like to do? Enter number 1-5: ')
		print('\t\t{:<20}'.format('1. Add entry'))
		print('\t\t{:<20}'.format('2. Update entry'))
		print('\t\t{:<20}'.format('3. Delete entry'))
		print('\t\t{:<20}'.format('4. Look up an entry'))
		print('\t\t{:<20}'.format('5. Quit'))

		inp_opt = input().strip()

		if inp_opt == '1':
			add_contact(contact_list)

		elif inp_opt == '2':
			update_contact(contact_list)

		elif inp_opt == '3':
			delete_contact(contact_list)

		elif inp_opt == '4':
			search_list = search_contact(contact_list)
			print('Below matching results are found:')
			show_contacts(search_list)
		
		elif inp_opt == '5':
			break
		
		else:
			print('Invalid input!!')

		store_book(contact_list, filename)

if __name__ == '__main__':
	main()

