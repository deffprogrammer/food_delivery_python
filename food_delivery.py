print("Welcome to Food Delivery App")
print("by Defa Mulya Pratama")

print("==========================")
print("1. Burger\t\t: 1500")
print("2. Chicken\t\t: 2500")
print("3. Hotdog\t\t: 3500")
print("4. French Fries\t: 4500")

total = 0
my_bool = True
while my_bool:
    option = input("Choose using number : ")
    amount = int(input("How many do you want to buy? : "))
    if option == "1":
        price = 1500 * amount
        total += price
    if option == "2":
        price = 2500 * amount
        total += price
    if option == "3":
        price = 3500 * amount
        total += price
    if option == "4":
        price = 4500 * amount
        total += price

    q_order = input("\nDo you want to add order?(y/n) : ")
    if q_order.lower() == "y":
        continue
    else:
        my_bool = False

print("\nTotal = ", total)

money = int(input("Enter your money : "))

if money < total:
    print("Your money is not enough")
else:
    money_changes = money - total
    print("Money Changes : ", money_changes)
    
print("\nThank you, see you later.....")

