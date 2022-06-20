command = input()

total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0

# Take prices without taxes until receive word special or regular for customer
while command != 'regular' and command != 'special':

    price = float(command)

    if price < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += price

    command = input()

# Check amount for taxes and total amount

total_amount_of_taxes = 0.2 * total_price_without_taxes
total_price_with_taxes = total_price_without_taxes + total_amount_of_taxes

# Discount 10% for special customer
if command == 'special':
    total_price_with_taxes *= 0.9

# Print the receipt if total price is not 0
if total_price_with_taxes == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")




