# Storefront is the main python file that the user interacts with
# Each employee will need to enter in their name to "login" as their
#sales will be tracked
import jsonpickle
from NewComputer import *
import pickle
from RefurbComputer import *
from Repair import *
#import sys
from time import *

print("Welcome to the Brown Family Computer & Repair Shop")
sleep(2)
print("Please choose from one of the following options: ")
sleep(2)
print("Press 1 to conduct a repair transation")
sleep(2)
print("Press 2 to sell a new computer")
sleep(2)
print("Press 3 to sell a refurbished computer")
sleep(2)
print("Press q to exit the program")
sleep(2)
transaction_choice = input("Enter here >>> ") #Change this verbiage for sure


if transaction_choice == 'q':
    print("Goodbye")

if transaction_choice == str(2):
    #maybe first print out a list of available NEW computers???
    print("Starting a new transaction for a new computer...")
    sleep(1)
    manufacturer_input = input("What type would the customer like (Apple, Dell, or Lenovo)? ")
    #print a list of available computers based on this input
    # Going to have to put a try/catch around this for manufacturers that we don't have in stock
    ram_input = input("How much RAM would the customer like (4GB, 8GB, or 16GB)? ")
    #print a list of available ram from the type that was entered
    storage_input = input("How much storage would the customer like (128GB, 256GB, 512GB, or 1TB)? ")
    #print a list of computer with the above configuration
    new_comp = NewComputer(manufacturer_input, ram_input, storage_input)
    #if this object matches one of the configurations in the pickle file, then mark it as sold
    print(new_comp)

    #writing a json file
    with open("new_comp_test.json", "a") as file:
        frozen = jsonpickle.encode(new_comp)
        file.write(frozen)

#reading a json file
    #with open("new_comp_test.json", "r") as file:
        #contents = file.read()
        #unfrozen = jsonpickle.decode(contents)
        #print(unfrozen)