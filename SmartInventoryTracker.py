
warehouse_a = {}
warehouse_b = {}
warehouse_c = {}
print("Input items into the warehouse")
print("Warehouse,Item,Quantity")
print("Type 'Done' when done inputting items")

a = warehouse_a
b = warehouse_b
c = warehouse_c

while True:
    print("***********************************************************")
    header = "\t WAREHOUSE INVENTORY "
    print(header)
    print("***********************************************************")
    print("1.Add items into the warehouses")
    print("2.Show master inventory")
    print("3.Show items in all warehouse")
    print("4.Show unique items in each warehouse")
    print("5.Show restock candidates")
    print("6.Show items shared between two warehouses")
    print("7.Exit")

    option = input("Please enter your choice.")

    if option == "1":
        while True:
            warehouse = input("Warehouse (a/b/c) :")
            if warehouse == "Done":
                break
            if warehouse not in ('a','b','c'):
                print("Invalid-Please input a/b/c!")    
                continue

            item = input("Item name : ")
            quantity = input("Quantity : ")
            if not quantity.isdigit():
                print("Quantity must be a number!")
                continue
            quantity = int(quantity)

            if warehouse == "a":
                a[item] = quantity
            elif warehouse == "b":
                b[item] = quantity
            elif warehouse == "c":
                c[item] = quantity
            else:
                print("Invalid,Please input a number!")        

# Master inventory
    elif option == "2":
    mi = master_inventory = {}

    for item in a :
        if item in mi :
            mi[item] += mi[item] + a[item]
        else :
            mi[item] = a[item]

    for item in b :
        if item in mi:
            mi[item] += mi[item] + b[item]
        else :
            mi[item] = b[item]           

    for items in c :
        if items in mi :
            mi[item] += mi[item] + c[item]
        else :
            mi[item] = c[item]

    print("Master Inventory : ", mi)   
    print("Master Inventory:", master_inventory)     

# items stocked in all warehouses
    elif option == "3":
    All_warehouses = []
    for item in a :
        if item in b and item in c:
            All_warehouses.append(item)
            print("items in all warehouses:", All_warehouses)


# items unique to each warehouse
    elif option == "4":
    unique_a = []
    for item in a :
        if item not in b and item not in c:
            unique_a.append(item)

    unique_b = []
    for item in a :
        if item not in a and item not in c :
            unique_b.append(item)

    unique_c = []
    for item in a :
        if item not in a and item not in b :
            unique_c.append(item)

    print("items unique to a:",unique_a)
    print("items unique to b:",unique_b)
    print("items unique to c:",unique_c)

# restock candidates
    elif option == "5":
    critical_items = {"laptop", "phone", "monitor", "camera", "scanner", "keyboard"}
    missing_items = []
    for item in critical_items :
        if item not in mi :
            missing_items.append(item)

    print("critical items missing:", missing_items)

# inventory movement plan
    elif option == "6":
    itemsinaandb = []
    itemsinaandc = []
    itemsinbandc = []

    for item in a and item in b :
        if item not in c :
            itemsinaandb.append(item)

    for item in a and item in c :
        if item not in b :
            itemsinaandc.append(item)

    for item in b and item in c :
        if item not in a :
            itemsinbandc.append(item)                

    print("items in a and b:", itemsinaandb)
    print("items in a and c:",itemsinaandc)
    print("items in b and c:",itemsinbandc)

# Exit
    elif option == "7": 
    print("Exiting Warehouse Inventory!")
    break
else: 
    print("Invalid.Please enter a number between 1-7!")