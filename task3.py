n = 20

print("Countdown from 20 to 0:")

#loop to print countdown

while n >= 0:

    print(n, " ", end = "")

    n = n - 1

print()  

print("Even number between 0 and 20, both inclusive: ")

#loop to print even numbers from 0 to 20, both inclusive

for i in range(21):

    if i%2 == 0:

        print(i, " ", end = " ")

print("\nPattern: ")        

#loops to print the pattern

for i in range(6):

    for j in range(i):

        print("*", end ="")

    print()    

    

print("GCD:")

#code to find GCD of two numbers

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))


x = 1

while x <= a and x <= b:

    if a % x == 0 and b % x == 0:

        gcd = x

    x = x + 1

 
print("The GCD of ", a, "and ", b, "is ", gcd)