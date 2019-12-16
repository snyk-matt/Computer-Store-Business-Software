import pandas as pd
import json
import numpy as np

file_name = 'testfile.csv'
"""
df = pd.DataFrame({'Make':['apple'], 'Model':['macbook'], 'RAM':['8'], 'Storage':['256'], 'RepairType':['screen'], 'RepairCost':['200'], 'RepairSellPrice':['300']})

pd.to_pickle(df, file_name)

unpickled_df = pd.read_pickle(file_name)

print(unpickled_df)

#with open(file_name, 'rb') as read_pickle_file:
#    repair_data = pickle.load(read_pickle_file)

#print(repair_data)

new_df = pd.DataFrame({'Make':['newapple'], 'Model':['newmacbook'], 'RAM':['new8'], 'Storage':['new256'], 'RepairType':['newscreen'], 'RepairCost':['new200'], 'RepairSellPrice':['new300']})

pd.concat([df, new_df], ignore_index)

#with open(file_name, 'wb') as write_pickle_file:
#df = df.append(update_df, ignore_index=True)

#print(update_df)
#print(df)
#print(repair_data)
"""
"""
df = pd.DataFrame({'Make':['apple'], 'Model':['macbook'], 'RAM':['8'], 'Storage':['256'], 'RepairType':['screen'], 'RepairCost':['200'], 'RepairSellPrice':['300']})

df.to_csv(file_name, index=False)

print(pd.read_csv(file_name))

new_df = pd.DataFrame({'Make':['newapple'], 'Model':['newmacbook'], 'RAM':['new8'], 'Storage':['new256'], 'RepairType':['newscreen'], 'RepairCost':['new200'], 'RepairSellPrice':['new300']})

new_df.to_csv(file_name, mode='a', index=False, header=False)
"""
#print(pd.read_csv(file_name))

#report_input = input("(1) To see a list available computers for sale " + "\n(2) To see refurbished computers for sale " + "\n(3) To see new computers for sale " + "\n>>> ")

file_name = 'Computer_Test.csv'
print("Retrieving report of available computers for sale... \n")
#sleep(1)
avail_inventory_df = pd.read_csv('Computer_Test.csv')
print(avail_inventory_df.loc[(avail_inventory_df['AvailableForSale']=='Y')].to_string(index=False) + "\n")
sell_input = int(input("Enter the serial number for the computer you'd like to sell: \n"))
testthing = avail_inventory_df[(avail_inventory_df['SerialNumber'] == sell_input)] 
otherthing = avail_inventory_df[(avail_inventory_df['AvailableForSale'] == 'N')]

df = pd.DataFrame(avail_inventory_df, index = [True, False, True, False])
print(df.iloc[1]) 


#print(data)
#if data:
#    print("This is correct")
#avail_inventory_df.loc[avail_inventory_df['SerialNumber'] == sell_input, 'AvailableForSale'] = 'N'

#avail_inventory_df.to_csv(file_name, index=False)

#print(avail_inventory_df.to_string(index=False) + "\n")