# Cumulative Sum of a Range
# Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
# Exercise Purpose: This exercise teaches “State Tracking.” In programming, you often need to remember a value from a previous loop iteration 
#   to calculate results in the current one. This is the basis for algorithms like Fibonacci sequences or running totals.
# Given Input: Range: numbers = range(10)

previous_nums = 0

for i in range(10):
    sum = previous_nums + i
    print(f"Current Number: {i}, Previous Number: {previous_nums}, Sum: {sum}")
    previous_nums = i
