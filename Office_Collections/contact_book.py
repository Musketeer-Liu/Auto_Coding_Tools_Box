import os
import pickle




datafile = 'contact.data'
line = '=============================='
message = '''
====================
Welcome Bookmark:
Press 1 to show list
Press 2 to add contact
Press 3 to edit contact
Press 4 to delete contact
Press 5 to search contact
Press 6 to show menu
Press 0 to quit
====================
'''
print(message)




class Contact(object):


    def __init__(self, name, number):
        self.name = name
        self.number = number




class Operation(object):


    def get_data(self, filename=datafile):
        if os.path.exists(filename) and os.path.getsize(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        return None


    def set_data(self, name, number, filename=datafile):
        contact_list = {} if self.get_data() == None else self.get_data()
        with open(filename, 'wb') as file:
            contact_list[name] = Contact(name, number)
            pickle.dump(contact_list, file)
    

    def save_data(self, contactbook, filename=datafile):
        with open(filename, 'wb') as file:
            pickle.dump(contactbook, file)
            
      
    def show_contact(self):
        contact_list = self.get_data()
        if contact_list:
            for contact in contact_list.values():
                print(contact.name, contact.number)
            print(line)
        else:
            print('Contact book is empty now, please add contact')     


    def add_contact(self, name, number):
        self.set_data(name, number)
        print('Contact added')
        print(line)

    
    def edit_contact(self, name, number):
        contact_list = self.get_data()
        if contact_list:
            if name in contact_list:
                contact_list[name] = Contact(name, number)
                self.save_data(contact_list)
                print('Contact edited')
            else: 
                print(name, ' is not in contact')
            print(line)


    def delete_contact(self, name):
        contact_list = self.get_data()
        if contact_list:
            if name in contact_list:
                del contact_list[name]
                self.save_data(contact_list)

            else:
                print(name, ' is not in contact')
            print(line)


    def search_contact(self, name):
        contact_list = self.get_data()
        if contact_list:
            if name in contact_list:
                print(contact_list[name].name, contact_list[name].number)
            else:
                print(name, 'is not in contact')
            print(line)
                



if __name__ == '__main__':
    operation = Operation()
    while True:
        code = input('Input Code >>')

        if code == '1':
            print('Show all contact list')
            operation.show_contact()

        elif code == '2':
            print('Add contact')
            name = input('Input Name >>')
            number = input('Input Number >>')
            operation.add_contact(name, number)

        elif code == '3':
            print('Edit contact')
            name = input('Input Name >>')
            number = input('Input Number >>')
            operation.edit_contact(name, number)

        elif code == '4':
            print('Delete Contact')
            name = input('Input Name >>')
            operation.delete_contact(name)

        elif code == '5':
            name = input('Input Name >>')
            operation.search_contact(name)

        elif code == '6':
            print(message)

        elif code == '0':
            break

        else: 
            print('Input Error | Please Retry')

