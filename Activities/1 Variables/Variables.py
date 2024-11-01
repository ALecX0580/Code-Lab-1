# Create variable storing string, then print value of name.
name = "Alen Alinas"
print("\033[2m1.\033[0m", name)
print()

# Define variable a and b, assign them the value 5 and 10. Then print the sum of a and b.
a = 5
b = 10
result = a + b
print("\033[2m2. \033[0mThe sum of", a, "and", b, "is:", result)  
print()

# Assign the string "Python is fun!" to a variable(message) and print it.
message = "Python is fun!"
print("\033[2m3.\033[0m", message)
print()

# Write a program to swap the value of two variables without using a third variable.
a = 24
b = 20
# Swap values
a = a + b
b = a - b
a = a - b
print("\033[2m4. \033[0m""Before swapping:", "a =", b, "and", "b =", a)
print(f"\tAfter swapping:", "a =", a, "and", "b =", b)
print()