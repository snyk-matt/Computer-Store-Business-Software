# Displays the sales assistant enhancement - shows the employees and what their sales
#are, as well as the profit each has generated
import os.path
import pandas as pd
import pathlib
import sys
from time import *

class SalesAssistant:

    users_logged_in = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def login(self):

        SalesAssistant.users_logged_in += 1
        return f"Hello, {self.first_name}, how can I help you today? \n"

    def add_new_user(self, first_name, last_name, phone_number):

        employee_df = pd.DataFrame(columns=['FirstName', 'LastName', 'PhoneNumber'])
    
        file_name = 'Current_Employees.csv'

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

        if os.path.isfile(file_name):
            print ("Updating Existing CSV file...")

            update_employee_df = pd.DataFrame({'FirstName':[self.first_name], 'LastName':[self.last_name], 'PhoneNumber':[self.phone_number]})
        
            update_employee_df.to_csv(file_name, mode='a', index=False, header=False)

        else:
            print ("Creating a new CSV file...")
        
            new_employee_df = pd.DataFrame({'FirstName':[self.first_name], 'LastName':[self.last_name], 'PhoneNumber':[self.phone_number]})
        
            new_employee_df.to_csv(file_name, index=False)

    def show_employees():
        print("Here is a list of all employees: \n")

        print(employee_df.to_string())

    #def remove_user(self):

    def logout(self):
        SalesAssistant.users_logged_in -= 1
        return f"{self.first_name} {self.last_name} has logged out"

    def sales_assistant_menu(self):

        sales_assistant_choice = input("Would you like to continue to work with the Sales Assistant? Enter any key to continue, or q to logout and exit: ").lower()

        if sales_assistant_choice == 'q':
            return False
        else:
            print("(1) to add a new employee to the system ")
            sleep(2)
            print("(2) to remove an employee from the system ")
            sleep(2)
            print("(3) to log your work hours ")
            sleep(2)
            print("Press q to log out and return to the main program ")

            return True