from tabulate import tabulate
from colorama import Fore, Style

menu = [
    {'dish_id': '1', 'dish_name': 'Margherita Pizza', 'price': 8.99, 'availability': True},
    {'dish_id': '2', 'dish_name': 'Pasta Carbonara', 'price': 12.99, 'availability': True},
    {'dish_id': '3', 'dish_name': 'Chicken Biryani', 'price': 10.99, 'availability': True},
]

orders = []

def display_menu():
    table = []
    for dish in menu:
        availability = Fore.GREEN + "Available" + Style.RESET_ALL if dish['availability'] else Fore.RED + "Not Available" + Style.RESET_ALL
        table.append([dish['dish_id'], dish['dish_name'], dish['price'], availability])
    headers = [Fore.CYAN + "Dish ID", "Dish Name", "Price", "Availability" + Style.RESET_ALL]
    print(tabulate(table, headers, tablefmt="fancy_grid"))

def add_dish():
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available? (yes/no): ").lower() == "yes"

    dish = {'dish_id': dish_id, 'dish_name': dish_name, 'price': price, 'availability': availability}
    menu.append(dish)
    print(f"{dish_name} has been added to the menu.")

def remove_dish():
    dish_id = input("Enter the dish ID to remove: ")
    for dish in menu:
        if dish['dish_id'] == dish_id:
            menu.remove(dish)
            print(f"Dish with ID {dish_id} has been removed from the menu.")
            return
    print(f"No dish found with ID {dish_id}.")

def update_availability():
    dish_id = input("Enter the dish ID to update availability: ")
    availability = input("Is the dish available? (yes/no): ").lower() == "yes"
    for dish in menu:
        if dish['dish_id'] == dish_id:
            dish['availability'] = availability
            print(f"Availability for dish with ID {dish_id} has been updated.")
            return
    print(f"No dish found with ID {dish_id}.")

def take_order():
    customer_name = input("Enter customer name: ")
    order_dishes = []
    while True:
        dish_id = input("Enter the dish ID (or press Enter to finish): ")
        if dish_id == "":
            break
        dish = next((dish for dish in menu if dish['dish_id'] == dish_id), None)
        if dish is None:
            print(f"No dish found with ID {dish_id}.")
        elif not dish['availability']:
            print(f"{dish['dish_name']} is not available.")
        else:
            order_dishes.append(dish)
            print(f"{dish['dish_name']} added to the order.")
    if len(order_dishes) > 0:
        order = {'order_id': len(orders) + 1, 'customer_name': customer_name, 'dishes': order_dishes, 'status': 'received'}
        orders.append(order)
        print("Order placed successfully.")
    else:
        print("No dishes added to the order.")
def update_order_status():
    try:
        order_id = int(input("Enter the order ID to update status: "))
        status = input("Enter the new status: ")

        for order in orders:
            if order['order_id'] == order_id:
                order['status'] = status
                print(f"Order {order_id} status updated to {status}.")
                return

        print(f"No order found with ID {order_id}.")
    except ValueError:
        print("Invalid order ID. Please enter a valid integer.")



def review_orders():
    if not orders:
        print("No orders placed yet.")
        return

    table = []
    for order in orders:
        dish_names = ', '.join([dish['dish_name'] for dish in order['dishes']])
        table.append([order['order_id'], order['customer_name'], dish_names, order['status']])
    headers = [Fore.CYAN + "Order ID", "Customer Name", "Dishes", "Status" + Style.RESET_ALL]
    print(tabulate(table, headers, tablefmt="fancy_grid"))

def main():
    while True:
        print("\n===== Welcome to Zesty Zomato =====")
        print("1. Display Menu")
        print("2. Add Dish to Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Exit")

        choice = int(input("Enter your choice (1-8): "))
        print()

        if choice == 1:
            display_menu()
        elif choice == 2:
            add_dish()
        elif choice == 3:
            remove_dish()
        elif choice == 4:
            update_availability()
        elif choice == 5:
            take_order()
        elif choice == 6:
            update_order_status()
        elif choice == 7:
            review_orders()
        elif choice == 8:
            print("Thank you for using Zesty Zomato. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
