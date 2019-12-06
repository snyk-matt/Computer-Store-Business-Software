# Class that will create a new sale object

#SerialNumber,Type,Condition,RAM,Storage,PurchasePrice,SalePrice,SoldFlag
#SN, Condition, SalePrice and SoldFlag will be predefined and no input is needed form user

class NewComputer:
    
    def __init__(self, manufacturer, ram, storage):
        self.manufacturer = manufacturer
        self.ram = ram
        self.storage = storage

    def __repr__(self):
        return "This is a new {} with {} of RAM and {} of storage".format(self.manufacturer, self.ram, self.storage)
