# Exercise 11. Removing Duplicates from a List
# Practice Problem: Write a script that takes a list containing duplicate items and returns a new list with only unique elements.


# Exercise Purpose: This exercise teaches “Data De-duplication.” In real-world data science, datasets are often “messy” with repeating entries. 
#   Mastering the conversion between Lists (which allow duplicates) and Sets (which do not) is the fastest way to clean data.

# Given Input: data = [1, 2, 2, 3, 4, 4, 4, 5]
# Expected Output: Unique List: [1, 2, 3, 4, 5]

def remove_dup(list):
    final_list = []
    for i in range(0, len(list)):
        if list[i] not in final_list: final_list.append(list[i])
    return final_list

unique_list = remove_dup([1, 2, 2, 3, 4, 4, 4, 5])
print(f'unique list: {unique_list}')