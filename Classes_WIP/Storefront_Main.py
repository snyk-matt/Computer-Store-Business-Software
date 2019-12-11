# Storefront is the main python file that the user interacts with
# Each employee will need to enter in their name to "login" as their
#sales will be tracked

import pickle
import sys
from time import *

print("Welcome to the Brown Family Computer & Repair Shop")
sleep(2)
print("Please choose from one of the following options: ")
sleep(2)
print("Press 1 to conduct a repair transation")
sleep(2)
print("Press 2 to see a list of available computer for sale")
sleep(2)
print("Press 3 to sell a new or refurbished computer")
sleep(2)
print("Press q to exit the program")
sleep(2)

transaction_choice = input("Enter here >>> ") #Change this verbiage for sure

while transaction_choice != 'q':

    if transaction_choice == str(1):
        print("Starting a new transaction for a repair...")
        sleep(1)
        make = input("Enter the number for the corresponding make 1. Apple 2. Lenovo or 3. Dell: ")
        #print a list of available computers based on this input
        # Going to have to put a try/catch around this for manufacturers that we don't have in stock
        ram = input("Choose from one of the following RAM options 1. 4GB 2. 8GB 3. 16GB: ")
        #print a list of available ram from the type that was entered
        storage = input("Choose from one of the following RAM options 1. 128GB 2. 256GB 3. 512GB 4. 1TB: ")

    
    if transaction_choice == str(2):
        #show a list of our computer inventory, both new and used
        #ask if they would like to make a transaction (press 1 to make a transaction?)
        #if they do make a transaction, make sure to mark it as sold
        print("Here is a list of computers in our inventory: ")

    if transaction_choice == str(3):
        # show the list of computers in the inventory to sell
        print("Which computer would you like to sell? ")
        #maybe use pickle.load to show the list, then update it

    if transaction_choice == 'q':
        print("Goodbye")
        sys.exit()
