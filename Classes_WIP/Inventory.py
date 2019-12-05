# Class that will get and display the models of computer that are for sale
# This will run various reports the employee can pull up

from csv import DictReader

with open("Inventory.csv") as inventoryFile:
    csv_reader = DictReader(inventoryFile)
    for row in csv_reader:
        # each row is an OrderedDict
        # Use this to print out multiple different reports
        # each row will print it's contents
        # i.e. to show types of computers in stock, run:
        print(row['Type'])
        # to show different RAM options in stock:
        print(row['RAM'])