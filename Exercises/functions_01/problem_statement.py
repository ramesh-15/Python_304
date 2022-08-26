# Problem statement


#===============================================================================Enter your number:5
#Given  sets of integers,  and , print their symmetric difference in ascending order.
#The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
"""Input Format
The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.
Sample Input:

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output
5
9
11
12"""
#main program
"""
num1=int(input("Enter your first range of set number:"))
num2=int(input("Enter your second range of set number:"))
set1=set()
set2=set()
print("first set values:")
for i in range(num1):
    ip=int(input("enter {} row element:".format(i)))
    set1.add(ip)
print("second set values:")
for i in range(num2):
    ip=int(input("enter {} row element:".format(i)))
    set2.add(ip)
print(set1.symmetric_difference(set2))"""


