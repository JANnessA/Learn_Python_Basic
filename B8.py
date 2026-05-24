# Exercise 8. String Reversal
# Practice Problem: Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

# Exercise Purpose: This exercise demonstrates “Sequence Slicing.” Strings in Python are sequences, 
#   and mastering the slicing syntax is a powerful shortcut for data manipulation that would take 5-10 lines of code in other languages.

# Given Input: text = "Python"
# 0 1 2 3 4 5

# Expected Output: Reversed: nohtyP

def reversal_string(text):
    result = ''
    for i in range (len(text) -1, 0, -1):
        result += text[i]
    return result

result = reversal_string('Python')
print(f'Reverse text {result}')