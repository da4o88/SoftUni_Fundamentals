number = int(input())

prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            prime = False
            break
if not prime:
    print("False")
else:
    print("True")
