import json
from datetime import datetime # import time so that you can get the accurate time for orders per hour
import matplotlib.pyplot as plt
from collections import Counter# counts the occurance of something in a list

# Menu Items
menu = {
    "1": "Coffee",
    "2": "Tea",
    "3": "Latte",
    "4": "Cappuccino",
    "5": "Espresso"
}

data_file = "orders.json"#This defines a file name (orders.json) where order data will be stored.


# Function to load orders from JSON
def load_orders():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Function to save orders to JSON
def save_orders(orders):
    with open(data_file, "w") as file:
        json.dump(orders, file, indent=4) # indent=4 makes it more readable


# Function to take an order
def take_order():
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}. {value}")
    choice = input("Select an item number: ")

    if choice in menu:
        order = {"item": menu[choice], "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        orders = load_orders()
        orders.append(order)
        save_orders(orders)
        print(f"Order for {menu[choice]} placed successfully!")
    else:
        print("Invalid selection. Try again.")


# Function to analyze orders
def analyze_orders():
    orders = load_orders()
    if not orders:
        print("No orders found.")
        return

    item_counts = Counter(order["item"] for order in orders)
    most_common = item_counts.most_common(1)[0] if item_counts else ("None", 0)

    order_times = [datetime.strptime(order["timestamp"], "%Y-%m-%d %H:%M:%S").hour for order in orders]
    orders_per_hour = Counter(order_times)

    print(f"Most popular item: {most_common[0]} ({most_common[1]} orders)")
    print("Orders per hour:")
    for hour, count in sorted(orders_per_hour.items()):
        print(f"{hour}:00 - {count} orders")

    # Optional: Generate a bar chart
    plt.bar(orders_per_hour.keys(), orders_per_hour.values())
    plt.xlabel("Hour of the Day")
    plt.ylabel("Number of Orders")
    plt.title("Orders Per Hour")
    plt.xticks(range(0, 24))
    plt.show()


# Main Menu
def main():
    while True:
        print("\n1. Place Order\n2. Analyze Orders\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            take_order()
        elif choice == "2":
            analyze_orders()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
