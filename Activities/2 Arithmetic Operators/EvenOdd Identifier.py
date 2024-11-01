# A program that asks for a number and prints whether it is even or odd using the modulus operator.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")