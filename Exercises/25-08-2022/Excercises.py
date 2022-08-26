#  Excercises
#  ----------

#===========================================================================

#1.Python Program to Check Whether a Given Number is Even or Odd using lambda?

#main program
"""
num=int(input("ente number:"))
Even_Odd=lambda x:x if x%2==0 else x
print(Even_Odd(num))"""



#===========================================================================

#2.Python Program to Find Sum of Digit of a Number using Recursion?

#main program
"""
def sum_recur(num):
    
    if num==0:
        return True
    else:
        return (num%10)+sum_recur(num//10)
num=int(input("ente number:"))
print(sum_recur(num))"""

#===========================================================================

#3.Python Program to Calculate the Power using Recursion?

#main program
"""
number=int(input("Enter your number:"))
power=2
def number_power(number,power):
    
    if power==0:
        return True
    else:
        
        return number*number_power(number,power-1)
print(number_power(number,power))"""

#===========================================================================
