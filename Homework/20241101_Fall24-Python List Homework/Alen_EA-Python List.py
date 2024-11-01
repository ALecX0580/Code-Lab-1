# Python List Exercises
print("\033[1m1. Creating a List\033[0m")
fruits = ["appple", "pineapple", "mango", "banana", "orange"]
print(fruits)
print("\n\033[1m2. Accessing Elements\033[0m")
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0], colors[2], colors[-1])
print("\n\033[1m3. Modifying a List\033[0m")
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print(numbers)
print("\n\033[1m4. List Slicing\033[0m")
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = []
subset.extend(names[:3])
print(subset)
print("\n\033[3mAlternative Code\033[0m") 
subset = names[:3]
print(subset)
print("\n\033[1m5. Looping through a List\033[0m")
num = (range(1, 11))
squared_num = []
for number in num:
    squared_num.append(number ** 2)
print(squared_num)
print("\n\033[1m6. List Methods: Append and Extend\033[0m")
shopping_cart = []
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
shopping_cart.extend(["butter", "cheese"])
print(shopping_cart)
print("\n\033[1m7. Finding Maximum and Minimum in a List\033[0m")
numbers = [45, 22, 88, 56, 92, 33]
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("\n\033[1m8. Counting Occurrences\033[0m")
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_of_a = letters.count("a")
print("Count of a is:", count_of_a)
print("\n\033[1m9. List Comprehension\033[0m")
squares_even = []
for x in range(1,11):
    if x % 2 == 0:
        squares_even.append(x**2)
print(squares_even)
print("\n\033[1m10. Removing Duplicates\033[0m")
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_num = list(set(nums))
print(unique_num)
print("\n\033[3mAlternative Code\033[0m") 
unique_num = []
for num in nums:
    if num not in unique_num:
        unique_num.append(num)
print(unique_num)