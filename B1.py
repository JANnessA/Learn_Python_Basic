# EX1: Arithmetic Product and Conditional Logic
# Practice Problem: Write a Python function that accepts two integer numbers. 
#   If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

# Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

#Given Input:
#   Case 1: number1 = 20, number2 = 30
#   Case 2: number1 = 40, number2 = 30
#Expected Output:
#   The result is 600
#   The result is 70

def product_or_sum (num1, num2):
    product = num1*num2

    if product <= 1000:
        return product
    else:
        return num1+num2
    
result = product_or_sum(20, 30)
print(f'the first result is {result}')

result = product_or_sum(40, 30)
print(f'the first result is {result}')