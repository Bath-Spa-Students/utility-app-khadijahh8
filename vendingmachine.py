# using chain dictionary to add a menu
chocolates = {
    "a1": {"item": "Kinder", "price": 3.0, "available amount": 10},
    "a2": {"item": "Galaxy", "price": 5.0, "available amount": 18},
    "a3": {"item": "Ferrero Rocher", "price": 9.0, "available amount": 30}
}

drinks = {
    "b1": {"item": "Red Bull", "price": 4.0, "available amount": 20},
    "b2": {"item": "Pepsi", "price": 2.0, "available amount": 15},
    "b3": {"item": "Sprite", "price": 2.0, "available amount": 13},
    "b4": {"item": "Water", "price": 1.0, "available amount": 20},
    "b5": {"item": "Iced Coffee", "price": 2.0, "available amount": 3}
}

chips = {
    "c1": {"item": "Lay's Tomato", "price": 2.0, "available amount": 10},
    "c2": {"item": "Lay's Cheese", "price": 2.0, "available amount": 2}
}

cim = 0  # Cash in machine

# printing categories menu
print("Welcome to my Vending Machine!")
print("Categories:")
print("a: Chocolates")
print("b: Drinks")
print("c: Chips")
print("-------------------------------------")

#aligning the main menu
def display_menu(products):
    print("{:<5} {:<15} {:<10} {:<8}".format("Code", "Item", "Price", "Stock"))
    print("-------------------------------------")
    for code, product in products.items():
        print("{:<5} {:<15} ${:<8.2f} {}".format(
            code, product['item'], product['price'], product['available amount']))

# using functions to take input from user
def select_category():
    return input("Select category (a, b, c): ")


def select_option(products):
    while True:
        option = input("Select an item: ")
        if option in products:
            return option
        else:
            print("Invalid item code. Please select a valid item code.")

# using while if method to control money in machine and change for user
def process_purchase(product, money):
    global cim
    while product['available amount'] > 0 and money < product['price']:
        print("Insufficient funds. Please insert more money.")
        user_money = float(input("Please insert more money: $"))
        money += user_money

    if product['available amount'] > 0:
        cim += product['price']  # Update cash in machine
        product['available amount'] -= 1  # Decrease stock
        change = money - product['price']
        print(f"Dispensing {product['item']}...")
        print(f"Thank you for your purchase! Enjoy your {product['item']}.")
        if change > 0:
            print(f"Change: ${change:.2f}")
        else:
            print("Exact amount inserted. No change given")
        return True
    elif product['available amount'] == 0:
        print(f"Sorry, {product['item']} is out of stock.")
    return False


# Example usage, displaying the choices in menu
category = select_category()

if category == 'a':
    display_menu(chocolates)
    option = select_option(chocolates)
    selected_product = chocolates[option]
    print(f"You selected: {selected_product['item']} - Price: ${selected_product['price']}")
    user_money = float(input("Please insert money: $"))
    process_purchase(selected_product, user_money)

elif category == 'b':
    display_menu(drinks)
    option = select_option(drinks)
    selected_product = drinks[option]
    print(f"You selected: {selected_product['item']} - Price: ${selected_product['price']}")
    user_money = float(input("Please insert money: $"))
    process_purchase(selected_product, user_money)

elif category == 'c':
    display_menu(chips)
    option = select_option(chips)
    selected_product = chips[option]
    print(f"You selected: {selected_product['item']} - Price: ${selected_product['price']}")
    user_money = float(input("Please insert money: $"))
    process_purchase(selected_product, user_money)
#if user enters invalid item- code
else:
    print("Invalid category selected.")