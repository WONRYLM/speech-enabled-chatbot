# SMART INVENTORY TRACKER
# Using dictionaries to create empty warehouses - For the user to input data/items
warehouse_a = {}
warehouse_b = {}
warehouse_c = {}

# Instructions how to input items into the warehouses
print("Input items into the warehouse")
print("Warehouse, Item, Quantity")
print("Type 'Done' when done inputting items")

# Shorter names for easier typing
a = warehouse_a
b = warehouse_b
c = warehouse_c

# Creating a loop for the main menu
while True:
    # Show the menu
    print("***********************************************************")
    header = "\tWAREHOUSE INVENTORY"
    print(header)
    print("***********************************************************")
    print("1. Add items into the warehouses")
    print("2. Show master inventory")
    print("3. Show items in all warehouses")
    print("4. Show unique items in each warehouse")
    print("5. Show restock candidates")
    print("6. Show items shared between two warehouses")
    print("7. Exit")

    # Obtain choices from the user
    option = input("Please enter your choice: ")

    # Option 1: Add items
    if option == "1":
        while True:
            warehouse = input("Warehouse (a/b/c) or 'Done' to stop: ")
            if warehouse == "Done":
                break
            if warehouse not in ('a', 'b', 'c'):
                print("Invalid - Please input a/b/c!")
                continue

            item = input("Item name: ")
            quantity = input("Quantity: ")
            if not quantity.isdigit():      #Ensure that the value given is a digit
                print("Quantity must be a number!")
                continue
            quantity = int(quantity)        #Make sure the value given is an integer

            # Store item in the correct warehouse
            if warehouse == "a":
                a[item] = quantity
            elif warehouse == "b":
                b[item] = quantity
            elif warehouse == "c":
                c[item] = quantity

    # Option 2: Show the master inventory
    elif option == "2":
        master_inventory = {}

        # Add items from warehouse A
        for item in a:
            if item in master_inventory:
                master_inventory[item] = master_inventory[item] + a[item]
            else:
                master_inventory[item] = a[item]

        # Add items from warehouse B
        for item in b:
            if item in master_inventory:
                master_inventory[item] = master_inventory[item] + b[item]
            else:
                master_inventory[item] = b[item]

        # Add items from warehouse C
        for item in c:
            if item in master_inventory:
                master_inventory[item] = master_inventory[item] + c[item]
            else:
                master_inventory[item] = c[item]

        # Shows the complete master inventory with everything inside it
        print("Master Inventory:", master_inventory)

    # Option 3: Show the items in all warehouses
    elif option == "3":
        all_warehouses = []                  #Empty list for all warehouses
        for item in a:
            if item in b and item in c:
                all_warehouses.append(item)  #Will add items that are present in all
        print("Items in all warehouses:", all_warehouses)

    # Option 4: Show unique items in each warehouse
    elif option == "4":
        unique_a = []
        for item in a:
            if item not in b and item not in c:
                unique_a.append(item)        #Will add items unique to warehouse a

        unique_b = []
        for item in b:
            if item not in a and item not in c:
                unique_b.append(item)        #Will add items unique to warehouse b

        unique_c = []
        for item in c:
            if item not in a and item not in b:
                unique_c.append(item)        #Will add items unique to warehouse c

        print("Items unique to A:", unique_a)
        print("Items unique to B:", unique_b)
        print("Items unique to C:", unique_c)

    # Option 5: Show restock candidates
    elif option == "5":
        # Build master inventory again 
        master_inventory = {}

        for item in a:
            if item in master_inventory:
                master_inventory[item] = master_inventory[item] + a[item]
            else:
                master_inventory[item] = a[item]

        for item in b:
            if item in master_inventory:
                master_inventory[item] = master_inventory[item] + b[item]
            else:
                master_inventory[item] = b[item]

        for item in c:
            if item in master_inventory:
                master_inventory[item] = master_inventory[item] + c[item]
            else:
                master_inventory[item] = c[item]

        # List of critical items that must be stocked
        critical_items = {"laptop", "phone", "monitor", "camera", "scanner", "keyboard"}
        missing_items = []

        # Find critical items that are missing
        for item in critical_items:
            if item not in master_inventory:
                missing_items.append(item)          #Will add items that are not in the master inventory

        print("Critical items missing:", missing_items)

    # Option 6: Show items shared between two warehouses
    elif option == "6":
        itemsinaandb = []
        itemsinaandc = []
        itemsinbandc = []

        # Find items in A and B but not in C
        for item in a:
            if item in b and item not in c:
                itemsinaandb.append(item)

        # Find items in A and C but not in B
        for item in a:
            if item in c and item not in b:
                itemsinaandc.append(item)

        # Find items in B and C but not in A
        for item in b:
            if item in c and item not in a:
                itemsinbandc.append(item)

        print("Items in A and B only:", itemsinaandb)
        print("Items in A and C only:", itemsinaandc)
        print("Items in B and C only:", itemsinbandc)

    # Option 7: Exit the program
    elif option == "7":
        print("Exiting!")
        break

    # If input by the user is invalid
    else:
        print("Invalid. Please enter a number between 1-7!")
