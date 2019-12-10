# Class that will create a new repair object, then store it into the repair inventory
import pickle

repair_order_nums = {

   #repair_number : (['Make', 'Model', 'RAM', 'Storage', 'RepairType', RepairCost, RepairSellPrice])
    1 : (['Apple', 'MacBook Pro', '8GB', '256GB', 'Screen', 200, 300]),
    2 : (['Dell', 'XPS 13', '4GB', '128GB', 'Keyboard', 100, 200]),
    3 : (['Lenovo', 'ThinkPad', '8GB', '512GB', 'Mother board', 300, 400])

}

with open('repair_orders_pick.pkl', 'wb') as repair_order_pickle_file:
  pickle.dump(repair_order_nums, repair_order_pickle_file)

with open('repair_orders_pick.pkl', 'rb') as repair_order_pickle_file:
  repair_data = pickle.load(repair_order_pickle_file)
  i = 1
  for repair_order_num in repair_data:
    print("Repair number " + str(repair_order_num) + ": " + str(repair_order_nums[i]))
    i += 1