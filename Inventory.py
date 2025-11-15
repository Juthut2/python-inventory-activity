items = []              
prices = {}     
        
while True:
    print("\n===== INVENTORY MENU =====")
    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] View Items")
    print("[4] Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("\nEnter item name: ")

        if name in items:
            print("Item already exists in the inventory!")
        else:
            try:
                price = float(input("Enter price: "))
                items.append(name)
                prices[name] = price
                print("Item added successfully!")
            except ValueError:
                print("Invalid price. Please enter a number.")

    elif choice == "2":
        name = input("\nEnter item name to update: ")
        if name in items:
            try:
                new_price = float(input("Enter new price: "))
                prices[name] = new_price
                print("Price updated successfully!")
            except ValueError:
                print("Invalid price. Please enter a number.")
        else:
            print("Item not found in the inventory.")

    elif choice == "3":
        print("\n===== CURRENT INVENTORY =====")
        if len(items) == 0:
            print("No items in the inventory.")
        else:
            for item in items:
                print(f"{item} - ₱{prices[item]}")

    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice. Please try again.")

#Justin Troy Rosalada Watermark
