# Storefront is the main python file that the user interacts with
# Each employee will need to enter in their name to "login" as their
#sales will be tracked

#import pathlib
import os.path
import pandas as pd
#import pickle
from Repair import *
import sys
from time import *

def menu():
    """This function runs at the end of each choice the user makes
    and asks if they want to make another transaction. If the user
    enters q, the program exits"""
    transaction_choice = input("Would you like to make a transaction? Enter any key to continue, or q to exit: ").lower()

    if transaction_choice == 'q':
        return False
    else:
        print("Press 1 to conduct a repair transaction")
        print("Press 2 to see a list of available computer for sale")
        print("Press 3 to sell a new or refurbished computer")
        print("Press q to exit the program")
        
        transaction_choice = input(">>> ")
        return True

def repair_select():

    print("Starting a new transaction for a repair...")
    sleep(1)
    make = input("Please enter the make: ")
    model = input("Please enter the model: ")
    ram = input("Please enter the RAM: ")
    storage = input("Please enter the storage capacity: ")
    repairType = input("Please enter the repair type: ")
    repairCost = input("Please enter the repair cost: ")
    repairSellPrice = input("Please enter the repair sell price: ")

    new_repair = Repair(make, model, ram, storage, repairType, repairCost, repairSellPrice)

def show_inventory():
    #This function shows the list of computers in inventory
    
    print("Here is a list of computers in our inventory: \n")
    sleep(1)
    inventory_df = pd.read_csv('Computer_Inventory.csv')
    print(inventory_df.to_string(index=False) + "\n")
    report_input = int(input("(1) To see a list available computers for sale " + "\n(2) To see refurbished computers available for sale " + "\n(3) To see new computers available for sale " + "\n>>> "))
    print(" ")

    #add try except block here***
    if report_input == 1:
        print("All computers available for sale: \n")
        print(inventory_df[inventory_df['AvailableForSale']=='Y'].to_string(index=False) + "\n")

    elif report_input == 2:
        print("Refurbished computers available for sale: \n")
        print(inventory_df.loc[(inventory_df['Condition'] == 'Refurbished') & (inventory_df['AvailableForSale'] == 'Y')].to_string(index=False) + "\n")
        
    elif report_input == 3:
        print("New computers available for sale: \n")
        print(inventory_df.loc[(inventory_df['Condition'] == 'New') & (inventory_df['AvailableForSale'] == 'Y')].to_string(index=False) + "\n")

    else:
        menu()

def sell_computer():
    #This function called when the user wants to sell a computer
    #show the list of computers in the inventory to sell
    #if it's sold, update the cell in csv to mark as sold
    file_name = 'Computer_Inventory.csv'
    print("Retrieving report of available computers for sale... \n")
    sleep(1)
    avail_inventory_df = pd.read_csv('Computer_Inventory.csv')
    print(avail_inventory_df.loc[(avail_inventory_df['AvailableForSale']=='Y')].to_string(index=False) + "\n")
    sell_input = int(input("Enter the serial number for the computer you'd like to sell: \n"))
    #avail_inventory_df.loc[(avail_inventory_df['SerialNumber'] == sell_input) & (inventory_df['AvailableForSale'] == 'N')]
    # ***NEED TO FIND OUT HOW TO MAKE BOOLEANS/CONDITIONALS***
    avail_inventory_df.loc[avail_inventory_df['SerialNumber'] == sell_input, 'AvailableForSale'] = 'N'
    avail_inventory_df.to_csv(file_name, index=False)
    print("Serial number " + sell_input + " was successfully sold and updated in the system. \n")

print("Welcome to the Brown Family Computer & Repair Shop")
sleep(2)
print("Please choose from one of the following options: ")
sleep(2)
print("Press 1 to conduct a repair transaction")
sleep(2)
print("Press 2 to see a list of available computer for sale")
sleep(2)
print("Press 3 to sell a new or refurbished computer")
sleep(2)
print("Press q to exit the program")
transaction_choice = input(">>> ")

while transaction_choice != 'q':

    if transaction_choice == str(1):
        
        repair_select()

        if not menu():
            print("Goodbye")
            sys.exit()
    
    if transaction_choice == str(2):
        
        show_inventory()
        
        if not menu():
            print("Goodbye")
            sys.exit()

    if transaction_choice == str(3):
        
        sell_computer()

        if not menu():
            print("Goodbye")
            sys.exit()

    if transaction_choice == 'q':
        print("Goodbye")
        sys.exit()