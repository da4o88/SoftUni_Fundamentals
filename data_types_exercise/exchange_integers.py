a = int(input())
b = int(input())

temp = a
print("Before:")
print(f"a = {a}")
print(f"b = {b}")

a = b
b = temp

print("After:")
print(f"a = {a}")
print(f"b = {b}")
