import pickle

# This will be a method used to pull up reports on current inventory stock

serial_nums = {

  #serial_number : (['Make', 'Model', 'Condition', 'RAM', 'Storage', 'Cost', 'SellPrice', 'SoldFlag'])

  1 : (['Apple', 'MacBook Pro', 'New', '8GB', '256GB', 1000, 1200, 'N']),
  2 : (['Apple', 'MacBook Air', 'New', '4GB', '128GB', 700, 900, 'N']),
  3 : (['Dell', 'XPS 13', 'Refurbished', '8GB', '512GB', 1100, 1300, 'N']),
  4 : (['Lenovo', 'ThinkPad', 'New', '8GB', '256GB', 900, 1100, 'N']),
  5 : (['Dell', 'XPS 15', 'New', '16GB', '1TB', 1300, 1600, 'N'])

}

with open('computer_sn_pick.pkl', 'wb') as comp_sn_pickle_file:
  pickle.dump(serial_nums, comp_sn_pickle_file)

with open('computer_sn_pick.pkl', 'rb') as comp_sn_pickle_file:
  computers = pickle.load(comp_sn_pickle_file)
  i = 1
  for serial_num in computers:
    print("Serial number " + str(serial_num) + ": " + str(serial_nums[i]))
    i += 1

test = 2

if test == 2:
  serial_nums[5][7] = 'Y'