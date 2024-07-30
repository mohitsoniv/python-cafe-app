'''
Create a python program to design a cafe menu, decies with their in the menu, when the coustmer order some item then item price will appear
or ask to add another item to order, and show the total payable amount of the order. 
'''
# Define the Cafe Menu 
menu = {
    "Pizza ": 150,
    "Samosa ": 20,
    "Momos ": 60,
    "Cold Drink ": 50,
    "Coffie ": 70,
}
# Greeting Message 
print("Welcome to Foody Club Cafe\n\n     --- Menu ---\n")

print("Pizza :       Rs 150/-\nSamosa :      Rs 20/-\nMomos :       Rs 60/-\nCold Drink :  Rs 50/-\nCoffie :      Rs 70/-\n")
order_total = 0 
item_1 = input("Enter the item Name = ")
if item_1 in menu :
    order_total += menu[item_1] # 0 + 50 = 50 
    print(f"Your {item_1} is order successfully.\n")
else :
    print(f"{item_1} is not available yet!")
another_order = input("Do you want to add another item? (Yes\\No) ")
if another_order == "Yes" :
    item_2 = input("Enter the another item = ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"{item_2} is added to order.")
else :
     print(f"Ordered item {item_2} is not avaialable!")
print(f"The total amount to pay is Rs {order_total}/-\n")
print("Thankyou for your Order!")

