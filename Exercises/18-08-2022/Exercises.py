
# team-2




#======================================================================================================================================

"""
1.Write a Python program to find a list of integers with exactly two occurrences of value 19 and at least three occurrences of value 5 in a list. 

Input: 

[19, 19, 15, 5, 3, 5, 5, 2] 

Output: 

True

#main program

lst=[int(x) for x in input("enter values:").split(',')]
if (lst.count(19)==2) and (lst.count(5)>=3):
    print("True")
else:
    print("False")

#output:
    
##enter values:19, 19, 15, 5, 3, 5, 5, 2
##True
##enter values:19, 19, 15, 5, 3, 5, 5, 2,19
##False   """
#======================================================================================================================================

#2.WAPP to check a given list of integers where the sum of the integers is equal to length of list.


#main program
"""
lst=[int(x) for x in input("enter values:").split(',')]
sum1=sum(lst)
if sum1==len(lst):
    print("equal")
else:
    print("not equal")

#output:
    
##enter values:19, 19, 15, 5, 3, 5, 5, 2
##not equal  """
#======================================================================================================================================

#3.WAPP to add two integers without using arithmetic operator?
"""
#main program

first=int(input("enter your first number:"))
second=int(input("enter your second number:"))
while second != 0:
    data = first & second
    first = first ^ second
    second = data << 1
print("result:",first)

#output:
##enter your first number:10
##enter your second number:15
##result: 25    """
#======================================================================================================================================
