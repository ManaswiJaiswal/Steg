print("Enter a number to be checked")
num = int(input())
counter = 0
for i in range(1, num +1):
    if (num % i) == 0:
        counter = counter +1

if counter == 2:
    print ("Number is prime")
else:
    print ("Number is composite")
