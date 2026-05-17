import storage

vending_machine = storage.load_inventory()
close = True
while close:
    vending_machine = [
    ["Coke", 25, 10],
    ["Sprite", 25, 8],
    ["Water", 15, 20],
    ["Chips", 20, 5],
    ["Chocolate", 30, 12]
]
    order = []
    print('''
Vending Machine (Project 7)
    1. Buy Item
    2. Check item count
    3. Restock items
    4. Exit
    ''')
    option = input("\nEnter your Option: ")

    if option.isdigit():
        if option == "1":
            print("\nVending Machine")
            print("Name    Price    Amount")
            for i in vending_machine:
                print(f"{i[0]:<10} ${i[1]:^3} {i[2]:>7}")
            item = input("\nEnter the name of the item you want to buy: ")
            found = False
            for i in vending_machine:
                if item == i[0]:
                    found = True
                    if i[2] > 0:
                        i[2] -= 1
                        print(f"You have bought {i[0]} for ${i[1]}.")
                        storage.save_inventory(vending_machine)
                        again = input("Do you want to make another transaction? (y/n): ")
                        if again.lower() == "y":
                            continue
                        elif again.lower() == "n":
                            print("Exiting..")
                            print("Done!")
                            close = False
                        else:
                            print("Invalid input, assuming no.")
                            close = False
                    else:
                        print(f"Sorry, {i[0]} is out of stock.")
                        close = False
            if not found:
                print("Sorry, we don't have that item. Try Again.")
        elif option == "2":
            print("\nItems in Stock:")
            print("Name    Price    Amount")
            for i in vending_machine:
                print(f"{i[0]:<10} ${i[1]:^3} {i[2]:>7}")
        elif option == "3":
            print("Restock Items")
            for i in vending_machine:
                print(f"{i[0]:<10} ${i[1]:^3} {i[2]:>7}")
            choice = input("Enter item name to restock: ")
            found = False
            for i in vending_machine:
                if choice == i[0]:
                    found = True
                    qty = input(f"How many {i[0]} to add? ")
                    if qty.isdigit() and int(qty) > 0:
                        i[2] += int(qty)
                        storage.save_inventory(vending_machine)
                        print("Restocked successfully.")
                    else:
                        print("Invalid quantity.")
            if not found:
                print("Invalid item name.")
        elif option == "4":
            print("Exiting..")
            print("Done!")
            close = False