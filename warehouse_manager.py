items = [
        {'name': 'coffee', 'quantity': 500, 'unit': 'kg', 'unit price (PLN)': 25.67 },
        {'name': 'inka', 'quantity': 345, 'unit': 'kg', 'unit price (PLN)': 12.45 },
        {'name': 'black tea', 'quantity': 769, 'unit': 'kg', 'unit price (PLN)': 7.09}
]

sold_items = []

def get_items(items):
    '''
    function that prints all the items stored in a list called: 'items'
    where each product is a dictionary of name, quantity, unit, and price per unit
    '''
    col_names = list(items[0].keys())
    #print(type(col_names))

    fmt = '{:<20} {:<15} {:<10} {:<10}'
    print(fmt.format(*col_names))
    col_space = ['-'*len(x) for i,x in enumerate(col_names)]
    print(fmt.format(*col_space))

    fmt = '{:<20} {:<12} {:<13} {:<10}'
    for i, x in enumerate(items):
            row = list(items[i].values())
            row = map(str, row)
            print(fmt.format(*row))

def add_items(items):
    '''
    function that adds items to the list of items in a magazine
    '''
    name = input('Give the name of the product: ')
    quantity = int(input('Give the quantity of the product: '))
    unit = input('Give the unit of the product (kg/l): ')
    unit_price = float(input('Give the price per unit of the product (PLN): '))
    items.append({'name': name, 'quantity': quantity, 'unit': unit, 'unit price (PLN)': unit_price})
    print(items)

def sell_items(items):

    '''
    function that checks if item is in the magazine with proper quantity and updates magazine state after
    successfull sale
    '''
    # list of all the items
    name_list =[]
    for i,x in enumerate(items): 
            name_list.append(items[i]['name'])
    #print(name_list)
    name = input('Please specify product you want to sell: ')
    if name not in name_list:
        return print('There is no such item in the catalog') 
    quantity = input('Please specify the quantity of the product (kg/l): ') 
    quantity = int(quantity)

    print(f'Item name: {name}')
    print(f'Quantity to sell: {quantity}')
    for i, x in enumerate(items):
                    
        if x['name'] == name and x['quantity'] > quantity:
                items[i]['quantity'] =  items[i]['quantity']-quantity
                print(f'Successfully sold {quantity} unit(s) of {name}')
                sold_items.append({'name': name, 'quantity': quantity, 'unit': items[i]['unit'], 'unit price (PLN)': items[i]['unit price (PLN)']})
        elif x['name'] == name and x['quantity'] < quantity:
                print('There is not enough quantity of the product in the magazine')

def get_costs(items):
    '''
    function that sums cost of items in the magazine
    '''
    cost = [x['quantity'] * x['unit price (PLN)'] for i, x in enumerate(items)]
    sum_cost = sum(cost)
    print(sum_cost)

def get_income(sold_items):
    '''
    function that sums income from items sold from the magazine
    '''
    cost = [x['quantity'] * x['unit price (PLN)'] for i, x in enumerate(sold_items)]
    income = sum(cost)
    print(income)

def show_revenue(items, sold_items):
    '''
    function shows revenue from the items that were sold in view to all the items that are in the magazine
    '''
    cost = [x['quantity'] * x['unit price (PLN)'] for i, x in enumerate(items)]
    sum_cost = sum(cost)
    income = [x['quantity'] * x['unit price (PLN)'] for i, x in enumerate(sold_items)]
    sum_income = sum(income)
    revenue = sum_income-sum_cost
    print(f'Income: {sum_income}')
    print(f'Costs: {sum_cost}')
    print('--------')
    print(f'Revenue: {revenue}')

def export_items_csv(items)
    '''
    saving current items in the magazine to csv file
    '''
    import csv
    with open('magazyn.csv', 'w') as csvfile:
    fieldnames = ['name', 'quantity', 'unit', 'unit price (PLN)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i,x in enumerate(items):
            writer.writerow(x)
            
def load_items_from_csv()
    '''
    loading items from a csv file into items list
    '''
        import csv
        items.clear
        with open('magazyn.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                items.append({row['name'], row['quantity'],row['unit'], row['unit price (PLN)']})

action = input('What would you like to do? ')


while action != 'exit':

    if action == 'get':
        get_items(items)
        action = input('What would you like to do? ')

    if action == 'add':
        add_items(items)
        action = input('What would you like to do? ')

    if action == 'sell':
        sell_items(items)
        action = input('What would you like to do? ')

    if action == 'cost':
        get_costs(items)
        action = input('What would you like to do? ')

    if action == 'income':
        get_income(sold_items)
        action = input('What would you like to do? ')

    if action == 'revenue':
        show_revenue(items, sold_items)
        action = input('What would you like to do? ')
    if action == 'save':
        export_items_csv(items)
        print('Successfully saved all items to the file, magazyn.csv')   
    if action == 'load':
        export_items_csv(items)
        print('Successfully loaded all items from the file, magazyn.csv')        

    if action == 'exit':
        print('exiting... Bye!')
        exit 