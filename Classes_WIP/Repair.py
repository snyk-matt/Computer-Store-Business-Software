import os.path
import pandas as pd
import pathlib
import sys

class Repair:

  def __init__(self, make, model, ram, storage, repairType, repairCost, repairSellPrice):

    df = pd.DataFrame(columns=['Make', 'Model', 'RAM', 'Storage', 'RepairType', 'RepairCost', 'RepairSellPrice'])
    
    file_name = 'Repairs.csv'

    self.make = make
    self.model = model
    self.ram = ram
    self.storage = storage
    self.repairType = repairType
    self.repairCost = repairCost
    self.repairSellPrice = repairSellPrice

    if os.path.isfile(file_name):
        print ("Updating Existing CSV file...")

        update_df = pd.DataFrame({'Make':[self.make], 'Model':[self.model], 'RAM':[self.ram], 'Storage':[self.storage], 'RepairType':[self.repairType], 'RepairCost':[self.repairCost], 'RepairSellPrice':[self.repairSellPrice]})
        
        update_df.to_csv(file_name, mode='a', index=False, header=False)

    else:
        print ("Creating a new CSV file...")
        
        new_df = pd.DataFrame({'Make':[self.make], 'Model':[self.model], 'RAM':[self.ram], 'Storage':[self.storage], 'RepairType':[self.repairType], 'RepairCost':[self.repairCost], 'RepairSellPrice':[self.repairSellPrice]})
        
        new_df.to_csv(file_name, index=False)