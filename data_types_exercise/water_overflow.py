number_of_litters = int(input())
total_water = 0
tank_capacity = 255
water_in_tank = 0

for i in range(number_of_litters):
    liters_of_water = int(input())
    total_water += liters_of_water

    if total_water <= tank_capacity:
        water_in_tank = total_water
    else:
        print(f"Insufficient capacity!")
        total_water -= liters_of_water

print(water_in_tank)
