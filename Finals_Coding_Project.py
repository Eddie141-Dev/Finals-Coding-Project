import storage
vending_machine = storage.load_inventory()
close = True
while close:
    order = []
    print("\nVending Machine")
    print("Name    Price    Amount")
    for i in vending_machine:
        print(f"{i[0]:<10} ${i[1]:^3} {i[2]:>7}")
    print('''
Vending Machine (Project 7)
    1. Buy Item
    2. Check item count
    3. Restock items
    4. Add new item
    5. Remove item
    6. Exit
    ''')
    option = input("\nEnter your Option: ")
    if storage.isadigit(option):
        if option == "1":
            item = input("\nEnter the name of the item you want to buy: ")
            found = False
            for i in vending_machine:
                if item == i[0]:
                    found = True
                    if i[2] > 0:
                        i[2] -= 1
                        print(f"You have bought {i[0]} for ${i[1]}.")
                        storage.save_inventory(vending_machine)
                        if not storage.again_loop():
                            close = False
                    else:
                        print(f"Sorry, {i[0]} is out of stock.")
                        close = True
            if not found:
                print("Sorry, we don't have that item. Try Again.")
                close = True
        elif option == "2":
            print("\nItems in Stock:")
            print("Name    Price    Amount")
            for i in vending_machine:
                print(f"{i[0]:<10} ${i[1]:^3} {i[2]:>7}")
        elif option == "3":
            access = input("Enter admin password to restock: ")
            if access != storage.vending_pass():
                print("Incorrect password. Access denied.")
                close = False
            else:
                print("Restock Items")
                choice = input("Enter item name to restock: ")
                found = False
                for i in vending_machine:
                    if choice == i[0]:
                        found = True
                        qty = input(f"How many {i[0]} to add? ")
                        if storage.isadigit(qty) and int(qty) > 20:
                            print("Cannot restock more than 20 items at a time.")
                            close = False
                        elif storage.isadigit(qty) and int(qty) > 0:
                            i[2] += int(qty)
                            storage.save_inventory(vending_machine)
                            print("Restocked successfully.")
                            if not storage.again_loop():
                                close = False
                        else:
                            print("Invalid quantity.")
                            close = True
                if not found:
                    print("Invalid item name.")
                    close = False
        elif option == "4":
            access = input("Enter admin password to add new item: ")
            if access != storage.vending_pass():
                print("Incorrect password. Access denied.")
                close = False
            else:
                name = input("Enter the name of the new item: ")
                price = input("Enter the price of the new item: ")
                amount = input("Enter initial stock of the new item: ")
                if not storage.inventory_limit():
                        close = False
                elif storage.isadigit(price) and storage.isadigit(amount):
                    vending_machine.append([name, int(price), int(amount)])
                    storage.save_inventory(vending_machine)
                    print("New item added successfully.")
                    if not storage.again_loop():
                        close = False
                if storage.isadigit(amount) and int(amount) > 20:
                    print("Cannot restock more than 20 items at a time.")
                    close = False
                elif not storage.isadigit(price) or not storage.isadigit(amount):
                    print("Invalid input. Please enter valid numbers for price and amount.")
                    close = False
        elif option == "5":
            access = input("Enter admin password to remove item: ")
            if access != storage.vending_pass():
                print("Incorrect password. Access denied.")
                close = False
            else:
                print("Select what item to remove:")
                for i in vending_machine:
                    print(f"{i[0]:<10} ${i[1]:^3} {i[2]:>7}")
                name = input("Enter the name of the item to remove: ")
                found = False
                for i in vending_machine:
                    if name == i[0]:
                        found = True
                        vending_machine.remove(i)
                        storage.save_inventory(vending_machine)
                        print("Item removed successfully.")
                        if not storage.again_loop():
                            close = False
                if not found:
                    print("Invalid item name.")
                    close = False
        elif option == "6":
            print("Exiting..")
            print("Done!")
            close = False
        else:
            print("Choice not in range. Try Again.")
            close = True
    else:
        print("Invalid Selection. Try Again")
