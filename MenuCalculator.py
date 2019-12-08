def Order_Menu(menu_dic):
    count = 1
    for key, value in menu_dic.items():
        print("{} {} - £{}".format(count, key, value))
        count += 1

def Calculate_Cost(order_no, menu_dic):
    item_list = list(order_no)
    items_ordered = []

    total_cost = 0
    for item in item_list:
        total_cost += list(menu_dic.values())[int(item) - 1]
        items_ordered += list(menu_dic.keys())[int(item)-1]  
    print("Total cost is: £{}".format(total_cost))
    return total_cost

menu = {'Chicken Strips': 3.5, 'French Fries': 2.50, 'Hamburger': 4, 'Hotdog': 3.5, \
    'Large Drink': 1.75, 'Medium Drink': 1.5, 'Milkshake': 2.25, 'Salad': 3.75, 'Small Drink': 1.25}

while True:
    Order_Menu(menu)
    print("Please enter which items you want from the menu, using the numbers")
    print("For example, if you want a French Fries a Hamburger and a Large drink enter: 235")
    order = input()
    Calculate_Cost(order, menu)