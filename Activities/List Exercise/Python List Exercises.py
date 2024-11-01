#Print the lust
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)
#Print an element of list by index
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
#Replace an element of list
animals = ["cat", "dog", "bird"]
animals[1] = "hamster"
animals[2] = "hedgehog"
print(animals)
#Adds an element to a list
colors = []
colors.append("red")
colors.append("green")
colors.append("blue")
print(colors)
colors.remove("green")
print(colors)
#Checks the amount of Elements in list
names = ["Alice", "Bob", "Charlie", "Diana"]
print("Length of the list:", len(names))
#Does math function using the Elemtents in list
numbers = [4, 7, 1, 8, 5]
total_sum = sum(numbers)
print("Sum of elemetns:", total_sum)
#Gets maximum and minimum
ages = [23, 45, 18, 34, 60]
print("Maximum age:", max(ages))
print("Minimum age:", min(ages))
#Sort list from least to most 
scores = [88, 56, 92, 78, 61]
scores.sort()
print("Sorted list:", scores)
#Checks if an element is in list
numbers = [1, 3, 5, 7, 9]
if 5 in numbers:
    print("Found!")
else:
    print("Not Found womp womp")
#Counts the number of elements within a list
items = [1, 2, 3, 4, 4, 4, 5]
count_of_4 = items.count(4)
print("Count of 4:", count_of_4)
#Extend the list by adding a list to another
list1 = [32, 42, 40, 50, 23]
list2 = [52, 23, 46]
list1.extend(list2)
print(list1)
#Reverse elements of the list from one side to the other
list1.reverse()
print(list1)
