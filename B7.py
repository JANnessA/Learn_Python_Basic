# Exercise 7. List Manipulation: Add and Remove

# Practice Problem: Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).

# Exercise Purpose: This exercise teaches “Dynamic Collection Management.” Lists are rarely static; being able to modify, expand, 
#   and prune them is essential for handling data like shopping carts, user lists, or inventory systems.

# Given Input: fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Expected Output: ['apple', 'cherry', 'date', 'elderberry', 'fig']

list_fruits = ["apple", "banana", "cherry", "date", "elderberry"]
list_fruits.append('fig')
list_fruits.pop(1)

print(list_fruits)