#task2

#===========================================================================

#1. WAP to triple all numbers of a given list of integers. Use Python map. Go to the editor
"""
nums = (1, 2, 3, 4, 5, 6, 7) 
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))"""
#===========================================================================

#2. Write a Python program to add three given lists using Python map and lambda. Go to the editor
"""nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 
print("Original list: ")
print(nums1)  
print(nums2)  
print(nums3)  
result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3) 
print("\nNew list after adding above three lists:")
print(list(result))"""

#===========================================================================

#3. Write a Python program to listify the list of given strings individually using Python map.
"""
color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print("Original list: ")
print(color) 
print("\nAfter listify the list of strings are:") 
result = list(map(list, color)) 
print(result)
"""
#===========================================================================

#4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map. Go to the editor
"""
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Base numbers abd index: ")
print(bases_num)
print(index)
result = list(map(pow, bases_num, index))
print("\nPower of said number in bases raised to the corresponding number in the index:")
print(result)"""
#===========================================================================

#5. Write a Python program to square the elements of a list using map() function. Go to the editor
"""
def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))"""
#===========================================================================

#6. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function. Go to the editor
"""
def change_cases(s):
  return str(s).upper(), str(s).lower()
 
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n",chrars)
 
result = map(change_cases, chrars)
print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))"""
#===========================================================================

#7. Write a Python program to add two given lists and find the difference between lists. Use map() function. Go to the editor
"""
def addition_subtrction(x, y):
    return x + y, x - y
 
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
print("Original lists:")
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print("\nResult:")
print(list(result))"""
#===========================================================================

#8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings. Go to the editor
"""
nums_list = [1,2,3,4]
nums_tuple = (0, 1, 2, 3) 
print("Original list and tuple:")
print(nums_list)
print(nums_tuple)
result_list = list(map(str,nums_list))
result_tuple = tuple(map(str,nums_tuple))
print("\nList of strings:")
print(result_list)
print("\nTuple of strings:")
print(result_tuple)"""

#===========================================================================

#9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer. Go to the editor
"""
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
print("Original data:")
print(student_data)
students_data_name = list(map(lambda x:x[0], student_data))
students_data_dob = list(map(lambda x:x[1], student_data))
students_data_weight = list(map(lambda x:int(x[2][:-2]), student_data))
print("\nStudent name:")
print(students_data_name)
print("Student name:")
print(students_data_dob)
print("Student weight:")
print(students_data_weight)"""

#===========================================================================

#10. Write a Python program to compute the square of first N Fibonacci numbers, using map function and generate a list of the numbers. Go to the editor

"""
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
print("Original data:")
print(student_data)
students_data_name = list(map(lambda x:x[0], student_data))
students_data_dob = list(map(lambda x:x[1], student_data))
students_data_weight = list(map(lambda x:int(x[2][:-2]), student_data))
print("\nStudent name:")
print(students_data_name)
print("Student name:")
print(students_data_dob)
print("Student weight:")
print(students_data_weight)"""
#===========================================================================

#11. Write a Python program to compute the sum of elements of a given array of integers, use map() function. Go to the editor
"""
from array import array
def array_sum(nums_arr):
    sum_n = 0
    for n in nums_arr:
        sum_n += n
    return sum_n

nums = array('i', [1, 2, 3, 4, 5, -15])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = array_sum(nums_arr)
print("Sum of all elements of the said array:")
print(result)"""
#===========================================================================

#12. Write a Python program to find the ration of positive numbers, negative numbers and zeroes in an array of integers. Go to the editor
"""
from array import array

def plusMinus(nums):
    n = len(nums)
    n1 = n2 = n3 = 0
    
    for x in nums:
        if x > 0:
            n1 += 1
        elif x < 0:
            n2 += 1
        else:
            n3 += 1
            
    return round(n1/n,2), round(n2/n,2), round(n3/n,2)

nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
nums = array('i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
print("\nOriginal array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)"""
#===========================================================================

#13. Write a Python program to count the same pair in two given lists. use map() function. Go to the editor
"""
from array import array

def plusMinus(nums):
    n = len(nums)
    n1 = n2 = n3 = 0
    
    for x in nums:
        if x > 0:
            n1 += 1
        elif x < 0:
            n2 += 1
        else:
            n3 += 1
            
    return round(n1/n,2), round(n2/n,2), round(n3/n,2)

nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
nums = array('i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
print("\nOriginal array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)"""
#===========================================================================

#14. Write a Python program to interleave two given list into another list randomly using map() function. Go to the editor
"""
import random
def randomly_interleave(nums1, nums2):
    result =  list(map(next, random.sample([iter(nums1)]*len(nums1) + [iter(nums2)]*len(nums2), len(nums1)+len(nums2))))
    return result
nums1 = [1,2,7,8,3,7]
nums2 = [4,3,8,9,4,3,8,9]
print("Original lists:") 
print(nums1)
print(nums2)
print("\nInterleave two given list into another list randomly:")
print(randomly_interleave(nums1, nums2))"""
#===========================================================================

#15. Write a Python program to split a given dictionary of lists into list of dictionaries using map function. Go to the editor
"""
import random
def randomly_interleave(nums1, nums2):
    result =  list(map(next, random.sample([iter(nums1)]*len(nums1) + [iter(nums2)]*len(nums2), len(nums1)+len(nums2))))
    return result
nums1 = [1,2,7,8,3,7]
nums2 = [4,3,8,9,4,3,8,9]
print("Original lists:") 
print(nums1)
print(nums2)
print("\nInterleave two given list into another list randomly:")
print(randomly_interleave(nums1, nums2))"""
#===========================================================================

#16. Write a Python program to convert a given list of strings into list of lists using map function. Go to the editor
"""
def strings_to_listOflists(str):
    result = map(list, str)
    return list(result)

colors = ["Red", "Green", "Black", "Orange"]
print('Original list of strings:')
print(colors)
print("\nConvert the said list of strings into list of lists:")
print(strings_to_listOflists(colors))"""
#===========================================================================

#17. Write a Python program to convert a given list of tuples to a list of strings using map function. Go to the editor
"""def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result   
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print("Original list of tuples:")
print(colors)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(colors))
names = [('Sheridan','Gentry'), ('Laila','Mckee'), ('Ahsan','Rivas'), ('Conna','Gonzalez')]
print("\nOriginal list of tuples:")
print(names)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(names))"""

#===========================================================================
