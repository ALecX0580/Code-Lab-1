# Python List Homework (Alen Efraim Alinas Cyber Security Level 4 | Yr1)

print("\033[1m1. Creating a List\033[0m")
# How to create a list. Initializes a list of fruits and square brakcets to store the values and prints it
fruits = ["appple", "pineapple", "mango", "banana", "orange"]
print(fruits)

print("\n\033[1m2. Accessing Elements\033[0m")
# Accessing specific elements of list. It accesses and prints the first, third, and last elements from list using indexing
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0], colors[2], colors[-1])

print("\n\033[1m3. Modifying a List\033[0m")
# Changing an element with another at a specific index and appending a new element at end of list 
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print(numbers)

print("\n\033[1m4. List Slicing\033[0m")
# Slicing to create a subset of the original list by taking the first 3 elements from the list named list
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print(subset)

print("\n\033[1m5. Looping through a List\033[0m")
# Iterating through a list using for loop. Creates list of numbers from 1 to 10 and appends the square of each number to new list
num = (range(1, 11))
squared_nums = []
for number in num:
    squared_nums.append(number ** 2)
print(squared_nums)

print("\n\033[1m6. List Methods: Append and Extend\033[0m")
# Starts with empty list, adds items one by one with append() and adds multiple items at once with extend()
shopping_cart = []
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
shopping_cart.extend(["butter", "cheese"])
print(shopping_cart)

print("\n\033[1m7. Finding Maximum and Minimum in a List\033[0m")
# Finding maximum and minimum values in list using max() and min()
numbers = [45, 22, 88, 56, 92, 33]
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

print("\n\033[1m8. Counting Occurrences\033[0m")
# Count the occurrences of specific element in list using count() function
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_of_a = letters.count("a")
print("Count of a is:", count_of_a)

print("\n\033[1m9. List Comprehension\033[0m")
# Creates new list containing squares of all even numbers from 1 to 10 using for loops and if-statement
squares_even = []
for x in range(1,11):
    if x % 2 == 0:
        squares_even.append(x**2)
print(squares_even)

print("\n\033[1m10. Removing Duplicates\033[0m")
# Converts list to a set and back to a list
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_num = list(set(nums))
print(unique_num)