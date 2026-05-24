# Exercise 12. List Comparison and Boolean Logic
# Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

# Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching 
#   and data integrity checks.

# Given Input:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# Expected Output:
# Given list: [75, 65, 35, 75, 30] | result is False
# Given list: [10, 20, 30, 40, 10] | result is True

def compare_text_first_and_last(text):
    if text[0] == text[len(text)-1]: return True
    else: return False

result = compare_text_first_and_last(numbers_x)
print(f'Given list: {numbers_x}, result is {result}')

result = compare_text_first_and_last(numbers_y)
print(f'Given list: {numbers_y}, result is {result}')