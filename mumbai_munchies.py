inventory = [
    {"id": 1, "name": "Chips", "price": 10, "available": True},
    {"id": 2, "name": "Biscuits", "price": 5, "available": True},
    {"id": 3, "name": "Candy", "price": 2, "available": False},
]

sales_records = []

def add_snack():
    snack_id = int(input("Enter snack ID: "))
    snack_name = input("Enter snack name: ")
    snack_price = float(input("Enter snack price: "))
    snack_available = input("Is snack available? (yes/no): ").lower() == "yes"

    snack = {"id": snack_id, "name": snack_name, "price": snack_price, "available": snack_available}
    inventory.append(snack)
    print("Snack added successfully!")

def remove_snack():
    snack_id = int(input("Enter snack ID to remove: "))

    for snack in inventory:
        if snack["id"] == snack_id:
            inventory.remove(snack)
            print("Snack removed successfully!")
            break
    else:
        print("Snack not found!")

def update_snack_availability():
    snack_id = int(input("Enter snack ID to update availability: "))

    for snack in inventory:
        if snack["id"] == snack_id:
            snack["available"] = not snack["available"]
            print("Snack availability updated successfully!")
            break
    else:
        print("Snack not found!")

def make_sale():
    snack_id = int(input("Enter snack ID sold: "))

    for snack in inventory:
        if snack["id"] == snack_id:
            if snack["available"]:
                snack["available"] = False
                sales_records.append(snack_id)
                print("Sale recorded successfully!")
            else:
                print("Snack is already sold out!")
            break
    else:
        print("Snack not found!")

def main():
    while True:
        print("----- Mumbai Munchies -----")
        print("1. Add a snack to inventory")
        print("2. Remove a snack from inventory")
        print("3. Update snack availability")
        print("4. Make a sale")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_snack()
        elif choice == "2":
            remove_snack()
        elif choice == "3":
            update_snack_availability()
        elif choice == "4":
            make_sale()
        elif choice == "5":
            print("Thank you for using Mumbai Munchies!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
