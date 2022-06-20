
def calculate_price(product, quantity):
    price = None
    if product == 'coffee':
        price = quantity * 1.5
    elif product == 'water':
        price = quantity * 1.0
    elif product == 'coke':
        price = quantity * 1.4
    elif product == 'snacks':
        price = quantity * 2.0

    return price


product = input()
quantity = int(input())
total_price = calculate_price(product, quantity)

print(f'{total_price:.2f}')
