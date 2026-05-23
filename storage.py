def Items(): 
    storage = open("Items.txt", "r", encoding="utf-8")
    contents = storage.read()
    storage.close()
    print(contents)
'''for reading the content of the file '''

def load_inventory():
    inventory = []
    stock = open("Items.txt", "r", encoding="utf-8")
    for line in stock:
        parts = line.strip().split()
        if len(parts) == 3:
            name, price, qty = parts
            inventory.append([name, int(price), int(qty)])
    stock.close()
    return inventory
'''for restokcking the items and for buying the items'''

def save_inventory(inventory):
    stock = open("Items.txt", "w", encoding="utf-8")
    for item in inventory:
        stock.write(f"{item[0]:<10} {item[1]:>3} {item[2]:>7}\n")
    stock.close()
'''for saving the updated inventory back to the file'''

def Vending_Pass():
    ID = "admin123"
    return ID
'''Password to access the vending machine'''

def again_loop():
    again = input("Do you want to make another transaction? (y/n): ")
    if again.lower() == "y":
        return True
    elif again.lower() == "n":
        print("Exiting..")
        print("Done!")
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return again_loop()
'''for asking the user if they want to make another transaction'''

def Inventory_limit():
    inventory = load_inventory()
    limit = 15
    if len(inventory) >= limit:
        print("Vending machine at max capacity. Cannot load more items.")
        return False
    return True